from rest_framework import serializers
from .models import *


# Serializers translate models and databases into Python datatypes which can be rendered into JSON for the API
# Model = the model to be serialized
# Fields = the fields of the model to appear in the API

class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = ('screening_id', 'reservation_type_id', 'reservation_contact', 'reserved', 'paid', 'cancelled')


class ScreeningSerializer(serializers.HyperlinkedModelSerializer):
    movie_id = serializers.StringRelatedField()
    room_id = serializers.StringRelatedField()

    class Meta:
        model = Screening
        fields = ('movie_id', 'room_id', 'screening_start')


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
                  'movie_duration', 'tickets_sold', 'certificate')


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transaction_type', 'date_time', 'amount', 'user_id', 'successful')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'email', 'password')
