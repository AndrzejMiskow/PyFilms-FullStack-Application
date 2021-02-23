from django.db import models
from django.utils.timezone import now
# from API_movies import Movie
# from API_users import User


class Reservation(models.Model):
    screening_id = models.ForeignKey('Screening', on_delete=models.CASCADE)
    reservation_type_id = models.ForeignKey('ReservationType', on_delete=models.CASCADE, null=False)
    reservation_contact = models.CharField(max_length=32, null=False, blank=False)
    reserved = models.BooleanField(default=False, null=False)
    paid = models.BooleanField(default=False, null=False)
    cancelled = models.BooleanField(default=False, null=False)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class ReservationType(models.Model):
    reservation_type = models.CharField(max_length=32, null=False, blank=False)


class Screening(models.Model):
    # movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE)
    screening_start = models.DateTimeField(default=now())


class Room(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False)
    seats_no = models.IntegerField()


class Seat(models.Model):
    row = models.IntegerField()
    number = models.IntegerField()
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)


class SeatReserved(models.Model):
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    screening_id = models.ForeignKey(Screening, on_delete=models.CASCADE)


