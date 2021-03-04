from django.test import TestCase
from .models import *


# Create your tests here.

class ApiTestCase(TestCase):

    # used to create dummy data, configure DB for testing etc.
    # prepares test fixture for tests to be conducted
    def setUp(self):
        # connect to DB or setup dummy DB with some data in it
        Movie.objects.create(movie_id=12, title="Avengers 7", director="Johnny Deep")

    # test adding a reservation to DB
    # def test_put_reservation(self):

    # test retrieving reservation entries from DB
    def test_get_reservation(self):
        film = Movie.objects.get(movie_id=12)
        self.assertEqual(film.title, "Avengers 7")
        self.assertEqual(film.director, "Johnny Deep")
