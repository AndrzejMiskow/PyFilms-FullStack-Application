from django.shortcuts import render
from django.views.generic import *

from API.models import *


def home(request):
    return render(request, 'Business.html', {})


def testChechkout(request):
    return render(request, "checkoutSimulation.html", {})


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

