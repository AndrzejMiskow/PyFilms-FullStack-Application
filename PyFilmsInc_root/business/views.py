from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import *
import datetime
from django.contrib import messages

from .forms import *
from API.models import *


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
        'pk': pk
    }

    return render(request, "checkoutSimulation.html", context)


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
                t_total = t_adult+t_child+t_senior

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
                        pk=((int(seat_nos[i])+541)+(32*(res.screening_id.room_id.name-1)))),
                        reservation_id=res, screening_id=screening)

    if request.method == "POST" and 'card-submit' in request.POST:
        return HttpResponseRedirect('/business/cardPayment/' + str(lead_booking))
    elif request.method == "POST" and 'cash-submit' in request.POST:
        return HttpResponseRedirect('/business/cashPayment' + str(lead_booking))


def testCash(request, **kwargs):
    if not authStaff(request):
        return HttpResponseRedirect('/customer/')
    pk = kwargs.get("pk")

    return render(request, "cashPayment.html", {})


def testCard(request, **kwargs):
    if not authStaff(request):
        return HttpResponseRedirect('/customer/')
    pk = kwargs.get("pk")

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
