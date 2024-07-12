import random

import pytest
from faker import Faker


from fixtures.booking.api import Create
from fixtures.booking.random import random_create

fake = Faker()


class TestBookingCreate:
    def test_create(self, url):
        """
        1. Try to create booking
        2. Check that status code 200
        3. Check response
        """
        body = random_create()
        create = Create(url=url)
        response = create.create_booking(body=body)
        assert response.status_code == 200

    @pytest.mark.parametrize('firstname', [fake.last_name(), fake.date_this_decade().isoformat(), 1234, True])
    def test_create_invalid_firstname(self, url, firstname):
        """
        1. Try to create booking with invalid value
        2. Check that status code 400
        3. Check response
        """
        body = {"firstname": firstname, "lastname": fake.last_name(), "totalprice": random.randint(100, 1000),
                "depositpaid": random.choice([True, False]),
                "bookingdates": {
                    "checkin": fake.date_this_decade().isoformat(),
                    "checkout": fake.date_between_dates(date_start=fake.date_this_decade(),
                                                        date_end=fake.future_date(end_date="+1y")).isoformat()
                },
                "additionalneeds": fake.word()}
        create = Create(url=url)
        response = create.create_booking(body=body)
        assert response.status_code == 400

    @pytest.mark.parametrize('totalprice', [fake.word(), fake.date_this_decade().isoformat(), '*', True])
    def test_create_totalprice_invalid(self, url, totalprice):
        """
        1. Try to create booking with invalid value
        2. Check that status code 400
        3. Check response
        """
        body = {"firstname": fake.first_name(), "lastname": fake.last_name(), "totalprice": totalprice,
                "depositpaid": random.choice([True, False]),
                "bookingdates": {
                    "checkin": fake.date_this_decade().isoformat(),
                    "checkout": fake.date_between_dates(date_start=fake.date_this_decade(),
                                                        date_end=fake.future_date(end_date="+1y")).isoformat()
                },
                "additionalneeds": fake.word()}
        create = Create(url=url)
        response = create.create_booking(body=body)
        assert response.status_code == 400
