from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'reservation', views.ReservationViewSet)
router.register(r'reservationtype', views.ReservationTypeViewSet)
router.register(r'screening', views.ScreeningViewSet)
router.register(r'room', views.RoomViewSet)
router.register(r'seat', views.SeatViewSet)
router.register(r'seatreserved', views.SeatReservedViewSet)
router.register(r'movie', views.MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
