from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, FileResponse
from django.views.generic import *
from django.db.models.functions import *
from django.db.models import Sum, Value, Count, Q
import datetime
from django.contrib import messages
from xhtml2pdf import pisa
from django.template.loader import get_template

from .forms import *
from API.models import *


# Functions used to determine if the current user is a member of staff or business owner
def authOwner(request):
    if request.user.is_superuser:
        return True
    else:
        messages.error(request, 'You must be an admin to view this page!')
        return False


def authStaff(request):
    if request.user.is_staff:
        return True
    else:
        messages.error(request, 'You must be a member of staff to view this page!')
        return False


def home(request):
    if not authStaff(request):
        return HttpResponseRedirect('/customer/')
    return render(request, 'Business.html', {})


# View which renders seating and where seats are chosen
def checkout(request, **kwargs):
    pk = kwargs.get("pk")
    # pk above is id of screening in DB for which to make the booking

    if not authStaff(request):
        return HttpResponseRedirect('/customer/')

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

    context = {
        'layout': layout,
        'pk': pk
    }

    return render(request, "checkoutSimulation.html", context)


# Creates a reservation and redirects to the appropriate payment page
def pay(request, **kwargs):
    if not authStaff(request):
        return HttpResponseRedirect('/customer/')

    lead_booking = 0
    if request.method == "POST":
        form = ReservationForm(request.POST)
        pk = kwargs.get("pk")
        screening = Screening.objects.get(pk=pk)

        if request.method == 'POST':
            form = ReservationForm(request.POST)
            seat_nos = request.POST.get('SelectedSeatsID').split(',')

            if form.is_valid():
                form = form.cleaned_data
                t_adult = form["tAdult"]
                t_child = form["tChild"]
                t_senior = form["tSenior"]
                t_total = t_adult + t_child + t_senior

                res = Reservation(screening_id=screening, reserved=True, paid=False, cancelled=False)
                lead_booking = res
                total_price = 0

                Movie.addTickets(screening.movie_id, t_total)

                for i in range(t_total):
                    res.pk = None
                    res.save()

                    if i == 0:
                        lead_booking = res.pk
                    else:
                        res.lead_booking = Reservation.objects.get(pk=lead_booking)

                    if i < t_adult:
                        res.reservation_type = Reservation.AD
                    elif i < (t_adult + t_child):
                        res.reservation_type = Reservation.CH
                    else:
                        res.reservation_type = Reservation.SE

                    res.save()
                    total_price += res.price

                    SeatReserved.objects.create(seat_id=Seat.objects.get(
                        pk=((int(seat_nos[i]) + 541) + (32 * (res.screening_id.room_id.name - 1)))),
                        reservation_id=res, screening_id=screening)

    if request.method == "POST" and 'card-submit' in request.POST:
        return HttpResponseRedirect('/business/cardPayment/' + str(lead_booking))
    elif request.method == "POST" and 'cash-submit' in request.POST:
        return HttpResponseRedirect('/business/cashPayment/' + str(lead_booking))


# Used to find every linked reservation and returns the lead booking and total price
def getReservationPrice(pk):
    lead_res = Reservation.objects.get(pk=pk)
    connected_res = Reservation.objects.filter(lead_booking=lead_res)

    price = lead_res.price

    if connected_res.count() != 0:
        for res in connected_res:
            price += res.price

    return price, lead_res


# Creates a transaction and redirects to the home page with a success message
def processPayment(request, **kwargs):
    pk = kwargs.get("pk")
    price, res = getReservationPrice(pk)
    kind = kwargs.get("type")

    # Transaction is linked to the member of staff handling the payment
    txn = Transaction.objects.create(transaction_type=kind, amount=price, booking=res, user_id=request.user,
                                     successful=True)
    txn.save()

    res.paid = True
    res.save()
    connected_res = Reservation.objects.filter(lead_booking=res)
    if connected_res.count() != 0:
        for ticket in connected_res:
            ticket.paid = True
            ticket.save()

    reservations = Reservation.objects.filter(Q(lead_booking=res) | Q(pk=res.pk))
    bookings = []

    # create 1 ticket per reservation
    for reservation in reservations:
        # adding data to the ticket template
        template_path = 'ticket.html'
        reserved_seat = SeatReserved.objects.filter(reservation_id=reservation.pk)
        reserved_seat = reserved_seat[0].seat_id
        context = {
            'name': "Ticket purchased at door",
            'seat': "Row " + str(reserved_seat.row) + ", Seat " + str(reserved_seat.number),
            'movie': reservation.screening_id.movie_id.title,
            'date_time': reservation.screening_id.screening_start,
            'room_id': reservation.screening_id.room_id,
            'res_type': reservation.reservation_type,
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

        bookings.append(filename)

    # display tickets as list
    context = {
        'bookings': bookings,
    }
    messages.success(request, "Reservation successful")
    return render(request, "viewTickets.html", context)


# Renders the UI for cash payments
def cashPayment(request, **kwargs):
    if not authStaff(request):
        return HttpResponseRedirect('/customer/')
    pk = kwargs.get("pk")
    price, lead_res = getReservationPrice(pk)

    context = {
        "price": price,
        "movie": lead_res.screening_id.movie_id.title,
        "pk": pk
    }

    return render(request, "cashPayment.html", context)


# Renders the UI for card payments
def cardPayment(request, **kwargs):
    if not authStaff(request):
        return HttpResponseRedirect('/customer/')
    pk = kwargs.get("pk")
    price, lead_res = getReservationPrice(pk)

    context = {
        "price": price,
        "movie": lead_res.screening_id.movie_id.title,
        "pk": pk
    }

    return render(request, "cardPayment.html", context)


def weeklyIncome(request):
    if not authOwner(request):
        return HttpResponseRedirect('/customer/')
    total_price = 0

    # Weekly income breakdown
    label = []
    data = []

    # Per Move breakdown
    label2 = []
    data2 = []

    total_movies = Reservation.objects.values('screening_id__movie_id__title').annotate(total=Sum('price'))

    print(total_movies)

    total_weekly = Reservation.objects.all().annotate(week=ExtractWeek('reserved_date')). \
        values('week'). \
        annotate(total=Sum('price'))

    total_overall = Reservation.objects.all()

    # Total Income of all time
    for res in total_overall:
        total_price += res.price

    extra_data = total_price

    for movie in total_movies:
        label2.append(movie["screening_id__movie_id__title"])
        data2.append(movie["total"])

    # weekly income used for graph
    for week in total_weekly:
        label.append(week["week"])
        data.append(week["total"])

    return render(request, 'WeeklyIncome.html', {
        'labels': label,
        'data': data,
        'extraData': extra_data,
        'label2': label2,
        'data2': data2,
    })


def ticketsSold(request):
    if not authOwner(request):
        return HttpResponseRedirect('/customer/')
    label = []
    data = []

    if request.method == "POST":
        from_date = request.POST.get('start')
        to_date = request.POST.get('end')

        movie_query = Reservation.objects.values('screening_id__movie_id__title').annotate(total=Count('price'))

        grouped_movies = movie_query.filter(reserved_date__range=[from_date, to_date])

        for movie in grouped_movies:
            label.append(movie['screening_id__movie_id__title'])
            data.append(movie['total'])

        return render(request, 'ticketsSold.html', {
            'labels': label,
            'data': data,
        })

    return render(request, 'ticketsSold.html', {
        'labels': label,
        'data': data,
    })


# show movies that can be booked
class MovieView(ListView):
    model = Movie
    template_name = 'selectMovie.html'


# show screenings for selected movie
def render_time_view(request, *args, **kwargs):
    if not authStaff(request):
        return HttpResponseRedirect('/customer/')

    pk = kwargs.get("pk")
    movie = Movie.objects.get(pk=pk)

    # generate range for today's datetime
    day_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    day_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)

    screenings = Screening.objects.filter(movie_id=pk, screening_start__range=(day_min, day_max))
    print(screenings)
    print(day_min)
    print(day_max)

    shows = {}

    for screening in screenings:
        shows[screening.screening_start.strftime("%H:%M")] = screening

    context = {
        "movie": movie,
        "screenings": shows,
    }

    return render(request, "selectTime.html", context)


# render pay for existing reservation page
def render_find_res(request):
    pk = None

    if not authStaff(request):
        return HttpResponseRedirect('/customer/')

    # redirect to payment using entered reservation ID
    if request.method == "POST":

        # get resID from forms
        form = FindResForm(request.POST)

        if form.is_valid():
            form = form.cleaned_data
            pk = str(form["resID"])
            lead_booking = Reservation.objects.get(pk=int(pk))

            # redirect if Reservation pk invalid
            if lead_booking is None:
                messages.error(request, 'Reservation with that ID not found. Please try again.')
                return HttpResponseRedirect('/business/findReservation')
            # otherwise check that reservation hasn't al;ready been paid for
            elif lead_booking.paid is True:
                messages.error(request, 'Reservation with that ID has already been paid for.')
                return HttpResponseRedirect('/business/findReservation')

        if 'card-submit' in request.POST:
            return HttpResponseRedirect('/business/cardPayment/' + pk)
        elif 'cash-submit' in request.POST:
            return HttpResponseRedirect('/business/cashPayment/' + pk)

    # otherwise request is GET and need to render page
    else:
        return render(request, "findReservation.html", {})
