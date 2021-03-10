from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import send_mail, EmailMessage

from API.models import Movie, Reservation


class HomeView(ListView):
    model = Movie
    template_name = 'home.html'


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movieDetails.html"


class BuyTickets(ListView):
    model = Movie
    template_name = 'buyTickets.html'


def render_ticket_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    reservation = get_object_or_404(Reservation, pk=pk)

    #adding data to the ticket template
    template_path = 'ticket.html'
    context = {
        'name': reservation.user_id.first_name + " " + reservation.user_id.last_name,
        'movie': reservation.screening_id.movie_id.title,
        'date_time': reservation.screening_id.screening_start,
        'room_id': reservation.screening_id.room_id,
        'res_type': reservation.reservation_type,
        'qrcode': reservation.qr_code,
    }

    # create file to contain the pdf
    filename = "ticket" + str(pk) + ".pdf"
    ticket = open("static/customer/tickets/"+filename, "w+b")

    # Find the template and render it
    template = get_template(template_path)
    html = template.render(context)

    # Create a pdf
    pisa_status = pisa.CreatePDF(html, dest=ticket)
    ticket.close()

    # if error then show alternative view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')


    # emailing ticket to user
    mail = EmailMessage(
        "Ticket(s) for " + reservation.screening_id.movie_id.title +
        " screening " + reservation.screening_id.screening_start.strftime("%H:%M %d/%m/%y"),
        "Dear " + reservation.user_id.first_name + ",\n\nPlease find attached your ticket. Enjoy the show!\n\nPyFilms Inc",
        None,
        [reservation.user_id.email],)

    # attaching the ticket.pdf to the email & sending it
    mail.attach_file('static/customer/tickets/'+filename)
    mail.send()
    
    #return to customer homepage
    return HttpResponseRedirect('/customer/')
