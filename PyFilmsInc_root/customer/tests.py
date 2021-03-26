from django.test import TestCase, Client
#from django.test.utils import setup_test_environment
from django.urls import reverse
from API.models import Movie
from customer.forms import ReservationForm


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
        new_movie = create_movie("1","Jack & Jill","John","A&B","Story about 2 lost kids","/",30,0,"U")
        response = self.client.get('/customer/')
        self.assertEqual(response.status_code , 200)
        self.assertQuerysetEqual(response.context['all_movies_list'],['<Movie: Jack & Jill>'])


class ReservationFormTest(TestCase):
    def test_fields_have_correct_label(self):
        form = ReservationForm()
        self.assertTrue(form.fields['saveCard'].label is None or form.fields['saveCard'].label ==
                        'saveCard')
        self.assertTrue(form.fields['cName'].label is None or form.fields['cName'].label == 'cName')
        self.assertTrue(form.fields['cNumber'].label is None or form.fields['cNumber'].label ==
                        'cNumber')
        self.assertTrue(form.fields['cExpiration'].label is None or form.fields['cExpiration'].label
                        == 'cExpiration')
        self.assertTrue(form.fields['cCVV'].label is None or form.fields['cCVV'].label == 'cCVV')

    def test_fields_initial_values(self):
        form = ReservationForm()
        self.assertEqual(form.fields['cName'].initial, '')
        self.assertEqual(form.fields['cNumber'].initial, '')
        self.assertEqual(form.fields['cExpiration'].initial, '')
        self.assertEqual(form.fields['cCVV'].initial, '')

    def test_card_number_field_correct_format(self):
        # card number less than 16 digits
        card_number1 = '111122223333'
        # card number more than 16 digits
        card_number2 = '11112222333344445'
        # card number exactly 16 digits
        card_number3 = '1111222233334444'
        data1 = {'qAdult': 1,
                 'qChild': 0,
                 'qSenior': 0,
                 'SelectedSeatsID': '0',
                 'cNumber': card_number1}
        data2 = {'qAdult': 1,
                 'qChild': 0,
                 'qSenior': 0,
                 'SelectedSeatsID': '0',
                 'cNumber': card_number2}
        data3 = {'qAdult': 1,
                 'qChild': 0,
                 'qSenior': 0,
                 'SelectedSeatsID': '0',
                 'cNumber': card_number3}
        form1 = ReservationForm(data1)
        self.assertFalse(form1.is_valid())
        form2 = ReservationForm(data2)
        self.assertFalse(form2.is_valid())
        form3 = ReservationForm(data3)
        self.assertTrue(form3.is_valid())

    def test_expiration_correct_format(self):
        card_number = '1111222233334444'
        # expiration1 - expiration4 should make form NOT valid
        expiration1 = '311/12'
        expiration2 = '13/20'
        expiration3 = '00/26'
        expiration4 = '12//25'
        expiration_correct = '12/25'
        data1 = {'qAdult': 1,
                 'qChild': 0,
                 'qSenior': 0,
                 'SelectedSeatsID': '0',
                 'cNumber': card_number,
                 'cExpiration': expiration1}
        data2 = {'qAdult': 1,
                 'qChild': 0,
                 'qSenior': 0,
                 'SelectedSeatsID': '0',
                 'cNumber': card_number,
                 'cExpiration': expiration2}
        data3 = {'qAdult': 1,
                 'qChild': 0,
                 'qSenior': 0,
                 'SelectedSeatsID': '0',
                 'cNumber': card_number,
                 'cExpiration': expiration3}
        data4 = {'qAdult': 1,
                 'qChild': 0,
                 'qSenior': 0,
                 'SelectedSeatsID': '0',
                 'cNumber': card_number,
                 'cExpiration': expiration4}
        data_correct = {'qAdult': 1,
                        'qChild': 0,
                        'qSenior': 0,
                        'SelectedSeatsID': '0',
                        'cNumber': card_number,
                        'cExpiration': expiration_correct}
        form1 = ReservationForm(data1)
        self.assertFalse(form1.is_valid())
        form2 = ReservationForm(data2)
        self.assertFalse(form2.is_valid())
        form3 = ReservationForm(data3)
        self.assertFalse(form3.is_valid())
        form4 = ReservationForm(data4)
        self.assertFalse(form4.is_valid())
        form_correct = ReservationForm(data_correct)
        self.assertTrue(form_correct.is_valid())

    def test_CVV_correct_format(self):
        card_number = '1111222233334444'
        expiration = '06/26'
        cvv_three = 123
        cvv_four = 1234
        cvv_two = 12
        cvv_five = 12345

        # data1 and data2 should make form valid, because their CVVs have exactly 3 or 4 digits
        data1 = {'qAdult': 1,
                'qChild': 0,
                'qSenior': 0,
                'SelectedSeatsID': '0',
                'cNumber': card_number,
                'cExpiration': expiration,
                'cCVV': cvv_three}
        data2 = {'qAdult': 1,
                 'qChild': 0,
                 'qSenior': 0,
                 'SelectedSeatsID': '0',
                 'cNumber': card_number,
                 'cExpiration': expiration,
                 'cCVV': cvv_four}

        # data3 and data4 should make form NOT valid, because their CVVs
        # don't have exactly 3 or 4 digits
        data3 = {'qAdult': 1,
                 'qChild': 0,
                 'qSenior': 0,
                 'SelectedSeatsID': '0',
                 'cNumber': card_number,
                 'cExpiration': expiration,
                 'cCVV': cvv_two}
        data4 = {'qAdult': 1,
                 'qChild': 0,
                 'qSenior': 0,
                 'SelectedSeatsID': '0',
                 'cNumber': card_number,
                 'cExpiration': expiration,
                 'cCVV': cvv_five}

        form1 = ReservationForm(data1)
        self.assertTrue(form1.is_valid())
        form2 = ReservationForm(data2)
        self.assertTrue(form2.is_valid())
        form3 = ReservationForm(data3)
        self.assertFalse(form3.is_valid())
        form4 = ReservationForm(data4)
        self.assertFalse(form4.is_valid())