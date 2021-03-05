from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from API.models import Movie, Reservation


class HomeView(ListView):
    model = Movie
    template_name = 'home.html'


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movieDetails.html"


def render_ticket_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    reservation = get_object_or_404(Reservation, pk=pk)

    template_path = 'ticket.html'
    context = {
        'name': reservation.user_id.first_name + " " + reservation.user_id.last_name,
        'movie': reservation.screening_id.movie_id.title,
        'date_time': reservation.screening_id.screening_start,
        'room_id': reservation.screening_id.room_id,
        'res_type': reservation.reservation_type
    }

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    # Uncomment next line to save file
    # response['Content-Disposition'] = 'attachment; filename="ticket.pdf"'

    # Find the template and render it
    template = get_template(template_path)
    html = template.render(context)

    # Create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show alternative view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


'''
    screening_id = models.ForeignKey('Screening', on_delete=models.CASCADE)
    reservation_type = models.CharField(max_length=32, null=False, blank=False,
                                        choices=RES_CHOICES, default=AD)
    reservation_contact = models.CharField(max_length=32, null=False, blank=False)
    reserved = models.BooleanField(default=False, null=False)
    paid = models.BooleanField(default=False, null=False)
    cancelled = models.BooleanField(default=False, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
'''