from django.http import HttpResponseRedirect
from django.shortcuts import render
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
    return render(request, "checkoutSimulation.html", {})


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
