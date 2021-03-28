from django.shortcuts import render
from django.views.generic import *
from django.db.models.functions import *
from django.db.models import Sum


from API.models import *



def home(request):
    return render(request, 'Business.html', {})


def testChechkout(request):
    return render(request, "checkoutSimulation.html", {})


def testCash(request):
    return render(request, "cashPayment.html", {})


def testCard(request):
    return render(request, "cardPayment.html", {})


def sampleGraph(request):
    TotalPrice = 0
    ChildTickets = 0
    SeniorTickets = 0

    label = []
    data = []


    TotalWeekly = Reservation.objects.all().annotate(week=ExtractWeek('reserved_date')).\
        values('week').\
        annotate(total=Sum('price'))


    for week in TotalWeekly:
        label.append(week["week"])
        data.append(week["total"])

    return  render(request , 'sampleGraphPage.html', {
        'labels' : label,
        'data' : data,
    })