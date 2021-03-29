from django.urls import include, path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('checkout/<pk>', checkout, name="checkout"),
    path('pay/<pk>', pay, name="payReservation"),
    path('cashPayment/<pk>', cashPayment, name="cashPayment"),
    path('cardPayment/<pk>', cardPayment, name="cardPayment"),
    path('selectMovie', MovieView.as_view(), name="selectMovie"),
    path('selectTime/<pk>', render_time_view, name="selectTime"),
    path('process/<type>/<pk>', processPayment, name="processPayment"),
    path('findReservation', render_find_res, name="findReservation"),
    path('weeklyIncome', weeklyIncome, name="weeklyIncome"),
    path('ticketsSolds', ticketsSold, name="ticketsSold"),
]
