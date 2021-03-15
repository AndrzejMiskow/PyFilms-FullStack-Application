from django.test import TestCase
from .models import *


# Create your tests here.
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

class MovieModelTests(TestCase):

    # used to create dummy data, configure DB for testing etc.
    # prepares test fixture for tests to be conducted
    def test__movie_insert(self):
        """
        To test if a record can be inserted into the MOVIE Model
        """
        # connect to DB or setup dummy DB with some data in it
        new_movie = create_movie("1","Jack & Jill","John","A&B","Story about 2 lost kids","/",30,0,"U")
        self.assertEqual(new_movie.movie_id,1)


    # test fail field insert 
        def test__fail_movie_insert(self):
            """
            To test if a record can be inserted into the MOVIE Model
            """
            # connect to DB or setup dummy DB with some data in it
            new_movie = create_movie("a","Bound to fail","Jack","B&C","Story about a failed test","/",30,0,"U")
            self.assertEqual(new_movie.movie_id,a)

    # def test_put_reservation(self):
