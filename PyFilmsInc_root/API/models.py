from django.db import models
from django.utils.timezone import now
from django.core.validators import MinLengthValidator


class Transaction(models.Model):
    CARD = "CARD"
    CASH = "CASH"

    PAY_CHOICES = [
        (CARD, "Card Payment"),
        (CASH, "Cash Payment")
    ]

    objects = models.Manager()
    transaction_type = models.CharField(max_length=32, null=False, blank=False,
                                        choices=PAY_CHOICES, default=CARD)
    date_time = models.DateTimeField(default=now())
    amount = models.FloatField()
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    successful = models.BooleanField(default=False, null=False)


class User(models.Model):
    objects = models.Manager()
    first_name = models.CharField(max_length=32, null=True)
    last_name = models.CharField(max_length=32, null=True)
    user_name = models.CharField(max_length=32, null=False, blank=False)
    email = models.EmailField(max_length=32, null=False, blank=False)
    password = models.CharField(max_length=32, validators=[MinLengthValidator(8)])


# database classes for Reservation tables
class Reservation(models.Model):
    AD = "ADULT"
    CH = "CHILD"
    SE = "SENIOR"
    ST = "STUDENT"

    RES_CHOICES = [
        (AD, "Adult"),
        (CH, "Child"),
        (SE, "Senior"),
        (ST, "Student")
    ]

    objects = models.Manager()
    # reservation_id = models.AutoField(primary_key=True, default=0)
    screening_id = models.ForeignKey('Screening', on_delete=models.CASCADE)
    reservation_type = models.CharField(max_length=32, null=False, blank=False,
                                        choices=RES_CHOICES, default=AD)
    reservation_contact = models.CharField(max_length=32, null=False, blank=False)
    reserved = models.BooleanField(default=False, null=False)
    paid = models.BooleanField(default=False, null=False)
    cancelled = models.BooleanField(default=False, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Screening(models.Model):
    objects = models.Manager()
    movie_id = models.ForeignKey('Movie', on_delete=models.CASCADE, null=True)
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE)
    screening_start = models.DateTimeField(default=now())


class Room(models.Model):
    objects = models.Manager()
    name = models.IntegerField()
    seats_no = models.IntegerField()

    def __str__(self):
        return str(self.name)


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
    movie_id = models.AutoField(primary_key=True, default=0)
    title = models.CharField(max_length=256, null=False, blank=False)
    director = models.CharField(max_length=256, null=False, blank=False)
    cast_members = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    # movie_poster = models.ImageField(upload_to='Movie_images', blank=True)
    movie_duration = models.IntegerField(null=False, blank=False)  # in minutes
    tickets_sold = models.IntegerField(default=0)
    certificate = models.CharField(max_length=2, default="U", null=False, blank=False)

    def __str__(self):
        return self.title
