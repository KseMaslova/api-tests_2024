import pytest
from faker import Faker

from fixtures.booking.api import Get
from fixtures.booking.random import random_get

fake = Faker()


class TestBookingGet:
    def test_get_booking_by_id(self, url):
        """
        1. Try to get booking with valid id
        2. Check that status code 200
        """
        url = f'{url}/booking'
        get = Get(url)
        response = get.get_booking(random_get())
        assert response.status_code == 200

    @pytest.mark.parametrize('id', ['fake.word()', '&!', None])
    def test_get_booking_invalid_id(self, url, id):
        """
        1. Try to get booking with invalid id
        2. Check that status code 404
        """
        url = f'{url}/booking'
        get = Get(url)
        response = get.get_booking(id)
        assert response.status_code == 404
