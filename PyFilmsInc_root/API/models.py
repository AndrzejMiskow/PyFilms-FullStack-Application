from django.db import models
from django.utils.timezone import now
# from API_movies import Movie
# from API_users import User

# database classes for Reservation tables
class Reservation(models.Model):
    objects = models.Manager()
    screening_id = models.ForeignKey('Screening', on_delete=models.CASCADE)
    reservation_type_id = models.ForeignKey('ReservationType', on_delete=models.CASCADE, null=False)
    reservation_contact = models.CharField(max_length=32, null=False, blank=False)
    reserved = models.BooleanField(default=False, null=False)
    paid = models.BooleanField(default=False, null=False)
    cancelled = models.BooleanField(default=False, null=False)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class ReservationType(models.Model):
    objects = models.Manager()
    reservation_type = models.CharField(max_length=32, null=False, blank=False)


class Screening(models.Model):
    objects = models.Manager()
    # movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE)
    screening_start = models.DateTimeField(default=now())


class Room(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=32, null=False, blank=False)
    seats_no = models.IntegerField()


class Seat(models.Model):
    objects = models.Manager()
    row = models.IntegerField()
    number = models.IntegerField()
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)


class SeatReserved(models.Model):
    objects = models.Manager()
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    screening_id = models.ForeignKey(Screening, on_delete=models.CASCADE)


# database classes for Movie tables
class Movie(models.Model):
    objects = models.Manager()
    movie_id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=256)
    director = models.CharField(max_length=256)
    cast_members = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    # movie_poster = models.ImageField(upload_to='Movie_images', blank=True)
    movie_duration = models.IntegerField(default=1)
    tickets_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.movie_text
