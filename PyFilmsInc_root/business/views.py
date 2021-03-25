from django.shortcuts import render
from django.views.generic import *
from API.models import *
import datetime

def home(request):
    return render(request, 'Business.html', {})


def checkout(request):
    pk = kwargs.get("pk")
    # pk above is id of screening in DB for which to make the booking
    
    context = {
    }
    
    return render(request, "checkoutSimulation.html", context)


def testCash(request):
    return render(request, "cashPayment.html", {})


def testCard(request):
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
    pk = kwargs.get("pk")
    movie = Movie.objects.get(pk=pk)
    
    # generate range for today's datetime
    dayMin = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    dayMax = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    
    screenings = Screening.objects.filter(movie_id = pk, screening_start__range = (dayMin, dayMax))
    shows = {}
    
    for screening in screenings:
        shows[screening.screening_start.strftime("%H:%M")] = screening
    
    context = {
        "movie": movie,
        "screenings": shows,
    }
    
    return render(request, "selectTime.html", context)