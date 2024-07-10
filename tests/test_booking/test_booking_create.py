from fixtures.booking.api import Create
from fixtures.booking.random import random_create

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