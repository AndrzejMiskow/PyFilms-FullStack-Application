from django.db import models
from django.db.models.signals import post_save
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.validators import MinLengthValidator
import qrcode
from django.core.files import File
from PIL import Image, ImageDraw
from io import BytesIO


class Profile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.IntegerField(unique=True, null=True, blank=True)
    exp_date = models.CharField(max_length=5, null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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
    date_time = models.DateTimeField(default=now)
    amount = models.FloatField()
    user_id = models.ForeignKey('Profile', on_delete=models.CASCADE)
    successful = models.BooleanField(default=False, null=False)


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
    screening_id = models.ForeignKey('Screening', on_delete=models.CASCADE)
    reservation_type = models.CharField(max_length=32, null=False, blank=False,
                                        choices=RES_CHOICES, default=AD)
    reservation_contact = models.CharField(max_length=32, null=False, blank=False)
    reserved = models.BooleanField(default=False, null=False)
    paid = models.BooleanField(default=False, null=False)
    cancelled = models.BooleanField(default=False, null=False)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    qr_code = models.ImageField(upload_to='static/customer/img/qr_codes', blank=True)

    # Overriding save function to generate a QR code when a reservation is saved
    def save(self, *args, **kwargs):
        # Generate a QR code with the primary key and user last name
        qrcode_img = qrcode.make(str(self.pk) + ':' + self.user_id.user.last_name)

        # Create a canvas on which to put the QR code
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{str(self.pk)}' + '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')

        # Save the file as a png in the static folder
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()

        # Continue with the usual saving
        super().save(*args, **kwargs)


class Screening(models.Model):
    objects = models.Manager()
    movie_id = models.ForeignKey('Movie', on_delete=models.CASCADE, null=True)
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE)
    screening_start = models.DateTimeField(default=now)


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
    poster_img = models.ImageField(upload_to='static/customer/img/',
                                   default='static/customer/img/default_movie.jpg',
                                   blank=False, null=False)
    movie_duration = models.IntegerField(null=False, blank=False)  # in minutes
    tickets_sold = models.IntegerField(default=0)
    certificate = models.CharField(max_length=2, default="U", null=False, blank=False)

    def __str__(self):
        return self.title
    
    def addTickets(count, self):
        self.tickets_sold += count
        self.save()