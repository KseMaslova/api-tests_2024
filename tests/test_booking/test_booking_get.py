import requests

from fixtures.booking.api import Get
from fixtures.booking.random import random_get


class TestBookingGet:
    def test_get_booking_by_id(self, url):
        url = random_get()
        #response = requests.get(url)
        get = Get(url)
        response = get.get()
        assert response.status_code == 200