from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import send_mail, EmailMessage
from .forms import *
from API.models import *
from django.contrib.auth.forms import UserCreationForm
import sys

from django.contrib.auth import login, authenticate


class HomeView(ListView):
    model = Movie
    template_name = 'home.html'


# generate movie detail page listing info about movie & available screenings
def render_movie_view(request, *args, **kwargs):
    pk = kwargs.get("pk")
    movie = get_object_or_404(Movie, pk=pk)
    screenings = Screening.objects.filter(movie_id=pk)

    # adding contents to context
    context = {
        'movie': movie,
        'screenings': screenings,
        # pk': pk,
    }

    # Renders and returns the template with the context
    return render(request, 'movieDetails.html', context)


# generate seat purchasing page
def render_purchase_view(request, *args, **kwargs):
    pk = None

    # get data
    if request.method == 'POST':

        form = ScreeningForm(request.POST)

        if form.is_valid():
            form = form.cleaned_data
            pk = int(form["screening"])

    # otherwise method is get        
    else:
        pass
        # pk = kwargs.get('pk')

    screening = get_object_or_404(Screening, pk=pk)
    seats = Seat.objects.filter(room_id=screening.room_id)

    # Generating a matrix to represent the seats and whether they're reserved
    rows = seats.last().row
    cols = seats.last().number
    current_col = 0
    current_row = 0
    layout = [["seat" for c in range(cols)] for r in range(rows)]

    for seat in seats:
        seat_reserved = SeatReserved.objects.filter(screening_id=screening, seat_id=seat).count()
        if seat_reserved != 0:
            layout[current_row][current_col] = "seat reserved"
        if current_col == cols - 1:
            current_row += 1
            current_col = 0
        else:
            current_col += 1

    # Applies the movie title and layout to the template
    context = {
        'movie': screening.movie_id.title,
        'layout': layout,
        'pk': pk
    }

    # Renders and returns the template with the context
    return render(request, 'buyTickets.html', context)


def render_ticket_views(request, screening_id, user_id):
    reservations = Reservation.objects.filter(screening_id=screening_id,
                                              user_id=Profile.objects.get(user=user_id))
    booking = reservations[0]
    tickets = []

    # emailing ticket to UserWarning
    mail = EmailMessage(
        "Ticket(s) for " + booking.screening_id.movie_id.title +
        " screening " + booking.screening_id.screening_start.strftime("%H:%M %d/%m/%y"),
        "Dear " + booking.user_id.user.first_name + ",\n\nPlease find attached your ticket. Enjoy the "
                                                    "show!\n\nPyFilms Inc",
        None,
        [booking.user_id.user.email], )

    # create 1 ticket per reservation
    for reservation in reservations:

        # adding data to the ticket template
        template_path = 'ticket.html'
        reservedSeat = SeatReserved.objects.filter(reservation_id=reservation.pk)
        reservedSeat = reservedSeat[0].seat_id
        context = {
            'name': reservation.user_id.user.first_name + " " + reservation.user_id.user.last_name,
            'seat': "Row " + str(reservedSeat.row) + ", Seat " + str(reservedSeat.number),
            'movie': reservation.screening_id.movie_id.title,
            'date_time': reservation.screening_id.screening_start,
            'room_id': reservation.screening_id.room_id,
            'res_type': reservation.reservation_type,
            'qrcode': reservation.qr_code,
            'poster': reservation.screening_id.movie_id.poster_img,
        }

        # create file to contain the pdf
        filename = "ticket" + str(reservation.pk) + ".pdf"
        ticket = open("static/customer/tickets/" + filename, "w+b")

        # Find the template and render it
        template = get_template(template_path)
        html = template.render(context)

        # Create a pdf
        pisa_status = pisa.CreatePDF(html, dest=ticket)
        ticket.close()

        # if error then show alternative view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')

        # attaching the ticket.pdf to the email & sending it
        mail.attach_file('static/customer/tickets/' + filename)

    mail.send()


# create entries for booking (reservations, transaction, seatReserveds)
def retrieve_make_booking(request, *args, **kwargs):
    pk = kwargs.get('pk')

    # get data
    if request.method == 'POST':

        form = ReservationForm(request.POST)
        reservation_count = 0
        seat_nos = request.POST.get('SelectedSeatsID').split(',')

        if form.is_valid():
            form = form.cleaned_data

            # make vars
            user = Profile.objects.get(user=request.user.id)
            q_adult = form["qAdult"]
            q_child = form["qChild"]
            q_senior = form["qSenior"]
            q_total = q_adult + q_child + q_senior

            save_card = form["saveCard"]
            c_number = form["cNumber"]
            c_exp = form["cExpiration"]

            res = Reservation(screening_id=Screening.objects.get(pk=pk), reserved=True, paid=True, cancelled=False,
                              user_id=user)
            lead_booking = res
            total_price = 0

            # update ticket sold quantity for Movie object 
            Movie.addTickets(q_total, Screening.objects.get(pk=pk).movie_id)

            # create reservation entry per party member
            for i in range(q_total):
                # auto-generate new res object with new pk
                res.pk = None
                res.save()

                # The first booking made is the "lead booking" and the others will be connected
                if i == 0:
                    lead_booking = res.pk
                else:
                    res.lead_booking = Reservation.objects.get(pk=lead_booking)

                if i < q_adult:
                    res.reservation_type = Reservation.AD
                elif i < (q_adult + q_child):
                    res.reservation_type = Reservation.CH
                else:
                    res.reservation_type = Reservation.SE

                res.save()
                total_price += res.price

                # create seat reservation for this party member
                SeatReserved.objects.create(
                    seat_id=Seat.objects.get(
                        pk=((int(seat_nos[i]) + 541) + (32 * (res.screening_id.room_id.name - 1)))),
                    reservation_id=res, screening_id=Screening.objects.get(pk=pk))

            # create transaction entry for reservation (fake card payment)
            if c_number == "":
                Transaction.objects.create(transaction_type=Transaction.CARD, amount=total_price, user_id=user,
                                           successful=True, booking=Reservation.objects.get(pk=lead_booking))

            # Save card details
            if save_card:
                user.card_number = c_number
                user.exp_date = c_exp
                user.save()

            # render tickets for every member & emails them to customer 
            render_ticket_views(request, res.screening_id, request.user.id)

    messages.success(request, 'Thanks! Your booking is confirmed, your ticket will arrive in your inbox soon.')
    return HttpResponseRedirect('/customer/')


# render user signup page
def render_signup_view(request):
    if request.method == "POST":

        # get user data from html page 
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            # validate & add email to user object
            email = request.POST.get('email')
            if len(email) > 0:
                user.email = email
                user.save()

            # validate & add name fields
            name = request.POST.get('first_name')
            surname = request.POST.get('surname')
            if (len(name) > 0) and (len(surname) > 0):
                user.first_name = name
                user.last_name = surname
                user.save()

            login(request, user)
            return HttpResponseRedirect('/customer/')

    # otherwise generate signup page
    else:
        form = UserCreationForm()

    # render page
    return render(request, 'signup.html', {'form': form})
