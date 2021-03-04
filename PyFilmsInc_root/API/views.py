from django.shortcuts import HttpResponse
from rest_framework import viewsets

from .serializers import *
from .models import *


# Create your views here.
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all().order_by('screening_id')
    serializer_class = ReservationSerializer


class ScreeningViewSet(viewsets.ModelViewSet):
    queryset = Screening.objects.all().order_by('screening_start')
    serializer_class = ScreeningSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('name')
    serializer_class = RoomSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all().order_by('room_id')
    serializer_class = SeatSerializer


class SeatReservedViewSet(viewsets.ModelViewSet):
    queryset = SeatReserved.objects.all().order_by('reservation_id')
    serializer_class = SeatReservedSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('movie_id')
    serializer_class = MovieSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('date_time')
    serializer_class = TransactionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer
