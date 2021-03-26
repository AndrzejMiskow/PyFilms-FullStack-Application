from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import *
from API.models import *
import datetime
from django.contrib import messages


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
    }

    return render(request, "checkoutSimulation.html", context)


def testCash(request):
    if not authStaff(request):
        return HttpResponseRedirect('/customer/')
    return render(request, "cashPayment.html", {})


def testCard(request):
    if not authStaff(request):
        return HttpResponseRedirect('/customer/')
    return render(request, "cardPayment.html", {})


class SampleBusinessPage(TemplateView):
    template_name = 'sampleGraphPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Movie.objects.all()
        return context


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
    shows = {}

    for screening in screenings:
        shows[screening.screening_start.strftime("%H:%M")] = screening

    context = {
        "movie": movie,
        "screenings": shows,
    }

    return render(request, "selectTime.html", context)
