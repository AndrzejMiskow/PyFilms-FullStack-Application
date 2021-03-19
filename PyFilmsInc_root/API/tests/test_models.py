from django.test import TestCase
from pytz import UTC
from API.models import *
import datetime


class TestUser(TestCase):

    def setUp(self):
        User.objects.create(id=45, first_name="Oliver", last_name="Smith",
                            username="user1234",
                            email="user1234@gmail.com",
                            password="userpassword1234")

    def test_user_full_name(self):
        user = User.objects.get(id=45)
        self.assertEqual(user.first_name, "Oliver")
        self.assertEqual(user.last_name, "Smith")

    def test_user_username(self):
        user = User.objects.get(id=45)
        self.assertEqual(user.username, "user1234")

    def test_user_password(self):
        user = User.objects.get(id=45)
        self.assertEqual(user.password, "userpassword1234")


class TestRoom(TestCase):

    def setUp(self):
        Room.objects.create(id=7, name=8, seats_no=50)

    def test_room_name(self):
        room = Room.objects.get(id=7)
        self.assertEqual(room.name, 8)

    def test_room_seat_no(self):
        room = Room.objects.get(id=7)
        self.assertEqual(room.seats_no, 50)

    def test_room_object(self):
        room = Room.objects.get(id=7)
        expected_object_name = str(room.name)
        self.assertEqual(expected_object_name, str(room))


class TestSeat(TestCase):

    def setUp(self):
        room = Room.objects.create(id=7, name=8, seats_no=50)
        Seat.objects.create(id=155, row=5, number=12, room_id=room)

    def test_seat_position(self):
        seat = Seat.objects.get(id=155)
        self.assertEqual(seat.row, 5)
        self.assertEqual(seat.number, 12)

    def test_seat_has_correct_room_id(self):
        seat = Seat.objects.get(id=155)
        self.assertEqual(seat.room_id.id, 7)
        self.assertEqual(seat.room_id.name, 8)


# class TestSeatReserved(TestCase):
#
#     def setUp(self):
#         movie = Movie.objects.create(title="Avengers: Infinity War", director="Joe Russo, "
#                                                                               "Anthony Russo",
#                                      cast_members="cast members...",
#                                      description="description...", movie_duration=160)
#         room = Room.objects.create(id=10, name=8, seats_no=50)
#         date_time = datetime.datetime(2021, 3, 25, 21, 0)
#         screening = Screening.objects.create(id=20, movie_id=movie, room_id=room,
#                                              screening_start=date_time)
#         reservation = Reservation.objects.create(id=5, screening_id=screening,
#                                                  reservation_type="SENIOR")
#         seat = Seat.objects.create(id=155, row=5, number=12, room_id=room)
#         SeatReserved.objects.create(id=201, seat_id=seat, reservation_id=reservation,
#                                     screening_id=screening)
#
#     def test_seat_reserved_has_correct_seat_id(self):
#         seat_reserved = SeatReserved.objects.get(id=201)
#         self.assertEqual(seat_reserved.seat_id.id, 155)
#         self.assertEqual(seat_reserved.seat_id.room_id.id, 10)
#         self.assertEqual(seat_reserved.seat_id.room_id.name, 8)
#
#     def test_seat_reserved_has_correct_reservation_id(self):
#         seat_reserved = SeatReserved.objects.get(id=201)
#         self.assertEqual(seat_reserved.reservation_id.id, 5)
#
#     def test_seat_reserved_has_correct_screening_id(self):
#         seat_reserved = SeatReserved.objects.get(id=201)
#         self.assertEqual(seat_reserved.screening_id.id, 20)


# class TestTransaction(TestCase):
#
#     def setUp(self):
#         date_time = datetime.datetime(2021, 5, 12, 18, 30)
#         user = User.objects.create(id=45, username="user1234", email="user1234@gmail.com",
#                                    password="userpassword1234")
#         profile1 = Profile.objects.create(user=user)
#         profile2 = Profile.objects.create(user=user)
#         Transaction.objects.create(id=102, date_time=date_time, amount=7.25, user_id=profile1)
#         Transaction.objects.create(id=103, transaction_type="CASH", date_time=date_time,
#                                    amount=7.25, user_id=profile2, successful=True)
#
#     def test_transaction_date_time_has_correct_format(self):
#         transaction = Transaction.objects.get(id=102)
#         date_time = datetime.datetime(2021, 5, 12, 18, 30, tzinfo=UTC)
#         self.assertEqual(date_time, transaction.date_time, "Transaction date_time does not have "
#                                                            "correct format")
#
#     def test_transaction_amount(self):
#         transaction = Transaction.objects.get(id=102)
#         self.assertEqual(transaction.amount, 7.25)
#
#     def test_transaction_has_correct_user(self):
#         transaction = Transaction.objects.get(id=102)
#         self.assertEqual(transaction.user_id.user.id, 45, "Transaction is not linked to correct "
#                                                           "user_id")
#         self.assertEqual(transaction.user_id.user.username, "user1234", "Transaction is not linked to "
#                                                                         "correct user_id")
#
#     def test_transaction_is_correct_type(self):
#         transaction1 = Transaction.objects.get(id=102)
#         transaction2 = Transaction.objects.get(id=103)
#         self.assertEqual(transaction1.transaction_type, "CARD", "Transaction default type "
#                                                                 "has wrong value")
#         self.assertEqual(transaction2.transaction_type, "CASH", "Transaction is of wrong type "
#                                                                 "when changed to CASH")
#
#     def test_transaction_successful(self):
#         transaction1 = Transaction.objects.get(id=102)
#         transaction2 = Transaction.objects.get(id=103)
#         self.assertEqual(transaction1.successful, False, "Transaction default 'successful' field "
#                                                          "should be set to False")
#         self.assertEqual(transaction2.successful, True, "Successful transaction should have "
#                                                         "'successful' field set to True")


# class TestReservation(TestCase):
#
#     def setUp(self):
#         movie = Movie.objects.create(movie_id=12, title="Avengers: Infinity War",
#                                      director="Joe Russo, Anthony Russo",
#                                      cast_members="Tom Holland, Chris Hemsworth, Scarlett "
#                                                   "Johansson, Robert Downey Jr., Chris Evans",
#                                      description="The Avengers must stop Thanos, an "
#                                                  "intergalactic warlord, from getting his "
#                                                  "hands on all the infinity stones. However, "
#                                                  "Thanos is prepared to go to any lengths to "
#                                                  "carry out his insane plan.",
#                                      movie_duration=160)
#
#         room = Room.objects.create(id=10, name=8, seats_no=50)
#         date_time = datetime.datetime(2021, 3, 25, 21, 0)
#
#         screening = Screening.objects.create(id=20, movie_id=movie, room_id=room,
#                                              screening_start=date_time)
#         Reservation.objects.create(id=5, screening_id=screening, reservation_type="SENIOR")
#         Reservation.objects.create(id=6, screening_id=screening)
#
#     def test_reservation_has_correct_screening(self):
#         reservation = Reservation.objects.get(id=5)
#         self.assertEqual(reservation.screening_id.id, 20, "Reservation contains wrong screening_id")
#         self.assertEqual(reservation.screening_id.movie_id.title, "Avengers: Infinity War")
#
#     def test_reservation_is_correct_type(self):
#         reservation1 = Reservation.objects.get(id=5)
#         reservation2 = Reservation.objects.get(id=6)
#         self.assertEqual(reservation1.reservation_type, "SENIOR", "Reservation is of wrong type "
#                                                                   "when changed default value")
#         self.assertEqual(reservation2.reservation_type, "ADULT", "Reservation default type has "
#                                                                  "wrong value")


class TestMovie(TestCase):

    def setUp(self):
        Movie.objects.create(movie_id=10, title="1917", director="Sam Mendes",
                             cast_members="George MacKay, Dean-Charles Chapman, "
                                          "Richard Madden, Benedict Cumberbatch, "
                                          "Andrew Scott",
                             description="During World War I, two British soldiers "
                                         "-- Lance Cpl. Schofield and Lance Cpl. "
                                         "Blake -- receive seemingly impossible "
                                         "orders. In a race against time, they must "
                                         "cross over into enemy territory to deliver "
                                         "a message that could potentially save 1,600 "
                                         "of their fellow comrades -- including "
                                         "Blake's own brother.",
                             movie_duration=119)

    def test_movie_title(self):
        movie = Movie.objects.get(movie_id=10)
        self.assertEqual(movie.title, "1917")

    def test_movie_director(self):
        movie = Movie.objects.get(movie_id=10)
        self.assertEqual(movie.director, "Sam Mendes")

    def test_movie_cast_members(self):
        movie = Movie.objects.get(movie_id=10)
        self.assertEqual(movie.cast_members, "George MacKay, Dean-Charles Chapman, Richard Madden, "
                                             "Benedict Cumberbatch, Andrew Scott")

    def test_movie_description(self):
        movie = Movie.objects.get(movie_id=10)
        self.assertEqual(movie.description, "During World War I, two British soldiers -- Lance Cpl."
                                            " Schofield and Lance Cpl. Blake -- receive seemingly "
                                            "impossible orders. In a race against time, they must "
                                            "cross over into enemy territory to deliver a message "
                                            "that could potentially save 1,600 of their fellow "
                                            "comrades -- including Blake's own brother.")

    def test_movie_duration(self):
        movie = Movie.objects.get(movie_id=10)
        self.assertEqual(movie.movie_duration, 119)

    def test_movie_object(self):
        movie = Movie.objects.get(movie_id=10)
        expected_object_name = movie.title
        self.assertEqual(expected_object_name, str(movie))


class TestScreening(TestCase):

    def setUp(self):
        movie = Movie.objects.create(movie_id=12, title="Avengers: Infinity War",
                                     director="Joe Russo, Anthony Russo",
                                     cast_members="Tom Holland, Chris Hemsworth, Scarlett "
                                                  "Johansson, Robert Downey Jr., Chris Evans",
                                     description="The Avengers must stop Thanos, an "
                                                 "intergalactic warlord, from getting his "
                                                 "hands on all the infinity stones. However, "
                                                 "Thanos is prepared to go to any lengths to "
                                                 "carry out his insane plan.",
                                     movie_duration=160)

        room = Room.objects.create(id=10, name=8, seats_no=50)
        date_time = datetime.datetime(2021, 3, 25, 21, 0)

        Screening.objects.create(id=20, movie_id=movie, room_id=room,
                                 screening_start=date_time)

    def test_screening_contains_correct_movie(self):
        screening = Screening.objects.get(id=20)
        self.assertEqual(screening.movie_id.movie_id, 12, "Screening contains wrong movie_id")
        self.assertEqual(screening.movie_id.title, "Avengers: Infinity War")

    def test_screening_contains_correct_room(self):
        screening = Screening.objects.get(id=20)
        self.assertEqual(screening.room_id.id, 10, "Screening contains wrong room_id")
        self.assertEqual(screening.room_id.name, 8)

    def test_screening_start_has_correct_format(self):
        screening = Screening.objects.get(id=20)
        date_time = datetime.datetime(2021, 3, 25, 21, 0, tzinfo=UTC)
        self.assertEqual(date_time, screening.screening_start, "screening_start does not have "
                                                               "correct format")

