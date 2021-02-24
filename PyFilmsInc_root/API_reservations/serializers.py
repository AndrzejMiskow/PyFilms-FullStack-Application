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
        fields = ('row', 'seat_no')


class SeatReservedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SeatReserved
        fields = ('seat_id', 'reservation_id', 'screening_id')
