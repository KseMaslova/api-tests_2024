import pytest
from faker import Faker

from fixtures.booking.api import Create
from fixtures.booking.random import random_create

fake = Faker()
import random

URL = "https://restful-booker.herokuapp.com/booking"


class TestBookingCreate:
    def test_create(self, url):
        """
        1. Try to create booking
        2. Check that status code 200
        3. Check response
        """
        body = random_create()
        create = Create(url=url)
        response = create.create(body=body)
        assert response.status_code == 200

    @pytest.mark.parametrize('firstname', ['fake.last_name()', 'fake.date_this_decade().isoformat()', 1234, True])
    def test_create_empty(self, url, firstname):
        body = {"firstname": firstname, "lastname": fake.last_name(), "totalprice": random.randint(100, 1000),
                "depositpaid": random.choice([True, False]),
                "bookingdates": {
                    "checkin": fake.date_this_decade().isoformat(),
                    "checkout": fake.date_between_dates(date_start=fake.date_this_decade(),
                                                        date_end=fake.future_date(end_date="+1y")).isoformat()
                },
                "additionalneeds": fake.word()}
        create = Create(url=url)
        response = create.create(body=body)
        assert response.status_code == 400
