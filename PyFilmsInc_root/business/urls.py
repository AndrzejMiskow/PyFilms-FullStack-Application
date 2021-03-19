from django.urls import include, path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('testCheckout', testChechkout, name="checkOut"),
    path('cashPayment', testCash, name="cashPayment"),
]
