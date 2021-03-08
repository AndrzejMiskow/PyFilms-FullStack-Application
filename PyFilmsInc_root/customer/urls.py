from django.urls import include, path
from .views import HomeView, MovieDetailView, BuyTickets

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('movie/<int:pk>', MovieDetailView.as_view(), name="movieDetails"),
    path('test', BuyTickets.as_view(), name="buyTickets"),
]
