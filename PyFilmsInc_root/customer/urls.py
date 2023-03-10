from django.contrib.auth import views as auth_views
from django.urls import path

from .views import *

urlpatterns = [
    path('', render_home, name="home"),
    path('movie/<pk>', render_movie_view, name="movieDetails"),
    path('tickets/', render_purchase_view, name="buyTickets"),
    path('booking/<pk>', retrieve_make_booking, name="booking"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="/customer/"), name="logout"),
    path('signup/', render_signup_view, name="signup"),
    path('account/', render_account_view, name="account"),
    path('bookings/', render_bookings_view, name="bookings"),
]
