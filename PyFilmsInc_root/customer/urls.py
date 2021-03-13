from django.urls import include, path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('movie/<int:pk>', MovieDetailView.as_view(), name="movieDetails"),
    path('tickets/<pk>', render_purchase_view, name="buyTickets"),
    path('booking/<pk>', retrieve_make_booking, name="booking"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    #path('logout/$', views.LogoutView, name="logout"),
]
