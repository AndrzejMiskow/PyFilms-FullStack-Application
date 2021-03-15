from django.test import TestCase, Client
from django.test.utils import setup_test_environment
from django.urls import reverse
from API.models import Movie


def create_movie(movie_id, title,director,cast_members,description,posterImg,
                 movie_duration,tickets_sold,certificate):
    """
    Method to create movie objects
    """
    return Movie.objects.create(movie_id=movie_id, title = title ,director = director,
                                cast_members = cast_members,description=description,
                                poster_img = posterImg, movie_duration = movie_duration,
                                tickets_sold = tickets_sold , certificate = certificate
                                )


# Create your tests here.
class CustomerListViewTest(TestCase):
    """
    Testing for responses from different URLS in the customer API
    """

    def test_no_movies(self):
        """
        To test /customer has no movies
        """
        response = self.client.get('/customer/')
        self.assertEqual(response.status_code , 200)
        self.assertQuerysetEqual(response.context['all_movies_list'],[ ])

    def test_current_movie_page(self):
        """
        To test /customer if it matches with the current number of movies in the Movie Model
        -NOTE This test would fail
        """
    #    new_movie = create_movie("1","Jack & Jill","John","A&B","Story about 2 lost kids","/",30,0,"U")
        response = self.client.get('/customer/')
        self.assertEqual(response.status_code , 200)
        self.assertQuerysetEqual(response.context['all_movies_list'],['<Movie: Black Widow>'])
