from django.urls import include, path
from .views import HomeView, MovieDetailView, render_ticket_view, render_purchase_view

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('movie/<int:pk>', MovieDetailView.as_view(), name="movieDetails"),
    path('test/<pk>', render_purchase_view, name="buyTickets"),
    path('ticket/<pk>', render_ticket_view, name="ticket")
]
