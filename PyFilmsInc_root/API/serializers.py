from rest_framework import serializers
from .models import *


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ('screening_id', 'reservation_type_id', 'reservation_contact', 'reserved', 'paid', 'cancelled')


class ReservationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReservationType
        fields = ('reservation_type', )


class ScreeningSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Screening
        fields = ('room_id', 'screening_start')


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('name', 'seats_no')


class SeatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seat
        fields = ('row', 'number', 'room_id')


class SeatReservedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SeatReserved
        fields = ('seat_id', 'reservation_id', 'screening_id')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'director', 'cast_members', 'description',
                  'movie_duration', 'tickets_sold')