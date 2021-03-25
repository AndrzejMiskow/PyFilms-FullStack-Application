from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import *
from django.contrib import messages

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


def testCheckout(request):
    if not authStaff(request):
        return HttpResponseRedirect('/customer/')

    screening = get_object_or_404(Screening, pk=1)
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

    # Gives the layout to the template
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


class SelectMovie(ListView):
    model = Movie
    template_name = 'selectMovie.html'
