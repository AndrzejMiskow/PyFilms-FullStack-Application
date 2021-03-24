from django.urls import include, path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('testCheckout', testChechkout, name="checkOut"),
    path('cashPayment', testCash, name="cashPayment"),
    path('cardPayment', testCard, name="cardPayment"),
    path('sampleGraph', SampleBusinessPage.as_view(), name="sampleGraph"),
    path('selectMovie' , SelectMovie.as_view() , name= "selectMovie"),
    path('selectTime' , SelectMovie.as_view() , name= "selectMovie"),
]
