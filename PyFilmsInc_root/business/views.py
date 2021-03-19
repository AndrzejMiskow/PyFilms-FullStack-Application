from django.shortcuts import render
from django.views.generic import ListView

from API.models import *


def home(request):
    return render(request, 'Business.html', {})


def testChechkout(request):
    return render(request, "checkoutSimulation.html", {})


def testCash(request):
    return render(request, "cashPayment.html", {})
