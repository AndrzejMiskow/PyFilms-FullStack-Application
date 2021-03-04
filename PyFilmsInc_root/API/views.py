from django.shortcuts import HttpResponse
from rest_framework import viewsets

from .serializers import *
from .models import *


# Each view corresponds to a serialized model - it decides what will be displayed to the user
# Queryset = which entries in the model to be displayed by default and how to order them
# Serializer_class = the serializer from serializers.py used for processing the model

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all().order_by('screening_id')
    serializer_class = ReservationSerializer


class ScreeningViewSet(viewsets.ModelViewSet):
    queryset = Screening.objects.all().order_by('movie_id')
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
