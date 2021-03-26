from django.urls import include, path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('checkout/<pk>', checkout, name="checkout"),
    path('pay/<pk>', pay, name="payReservation"),
    path('cashPayment/<pk>', cashPayment, name="cashPayment"),
    path('cardPayment/<pk>', cardPayment, name="cardPayment"),
    path('sampleGraph', SampleBusinessPage.as_view(), name="sampleGraph"),
    path('selectMovie', MovieView.as_view(), name="selectMovie"),
    path('selectTime/<pk>', render_time_view, name="selectTime"),
    path('process/<type>/<pk>', processPayment, name="processPayment")
]
