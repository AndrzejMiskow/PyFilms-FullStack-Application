from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Reservation)
admin.site.register(Screening)
admin.site.register(Movie)
admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(SeatReserved)
admin.site.register(Profile)
admin.site.register(Transaction)
