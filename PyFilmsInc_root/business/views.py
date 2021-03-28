from django.shortcuts import render
from django.views.generic import *
from django.db.models.functions import *
from django.db.models import Sum, Value


from API.models import *



def home(request):
    return render(request, 'Business.html', {})


def testChechkout(request):
    return render(request, "checkoutSimulation.html", {})


def testCash(request):
    return render(request, "cashPayment.html", {})


def testCard(request):
    return render(request, "cardPayment.html", {})


def weeklyIncome(request):
    TotalPrice = 0
    ChildTickets = 0
    SeniorTickets = 0

    #Weekly income breakdonw
    label = []
    data = []

    #Per Moive breakdown
    label2 = []
    data2 = []

    #hold total income
    extraData = []


    TotalMovies = Reservation.objects.values('screening_id__movie_id__title').annotate(total=Sum('price'))

    print(TotalMovies)

    TotalWeekly = Reservation.objects.all().annotate(week=ExtractWeek('reserved_date')).\
        values('week').\
        annotate(total=Sum('price'))

    TotalOverall = Reservation.objects.all()

    #Total Income of all time
    for res in TotalOverall:
        TotalPrice += res.price

    extraData.append(TotalPrice)

    for movie in TotalMovies:
        label2.append(movie["screening_id__movie_id__title"])
        data2.append(movie["total"])

    #weekly income used for graph
    for week in TotalWeekly:
        label.append(week["week"])
        data.append(week["total"])

    return  render(request , 'WeeklyIncome.html', {
        'labels' : label,
        'data' : data,
        'extraData' : extraData,
        'label2' : label2,
        'data2' : data2,
    })