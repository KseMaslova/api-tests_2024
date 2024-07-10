import pytest

from conftest import url
from fixtures.auth.api import Auth


class TestAuth:
    def test_auth_valid_data(self, url):
        """
        1. Try to auth
        2. Check that status code 200
        3. Check response
        """
        body = {"username": "admin", "password": "password123"}
        auth = Auth(url=url)
        response = auth.auth(body=body)
        assert response.status_code == 200

    @pytest.mark.parametrize('username', ['admin@.com', '1234', '_&!', 'test', 'Admin', True])
    def test_auth_invalid_username(self, username, url):
        """
        1. Try to auth with invalid username
        2. Check that status code 400
        3. Check response
        """
        body = {"username": username, "password": "password123"}
        auth = Auth(url=url)
        response = auth.auth_1(body=body)
        assert response.status_code == 400

    @pytest.mark.parametrize('password', ['test@test', 'password111', 'test', 1234, True])
    def test_auth_invalid_password(self, password, url):
        """
        1. Try to auth with invalid password
        2. Check that status code 400
        3. Check response
        """
        body = {"username": "admin", "password": password}
        auth = Auth(url=url)
        response = auth.auth_1(body=body)
        assert response.status_code == 400

    def test_auth_empty_username(self, url, username=None):
        """
        1. Try to auth with empty username
        2. Check that status code 400
        3. Check response
        """
        body = {"username": username, "password": "password123"}
        auth = Auth(url=url)
        response = auth.auth_1(body=body)
        assert response.status_code == 400

    def test_auth_empty_password(self, url, password=None):
        """
        1. Try to auth with empty password
        2. Check that status code 400
        3. Check response
        """
        body = {"username": "admin", "password": password}
        auth = Auth(url=url)
        response = auth.auth_1(body=body)
        assert response.status_code == 400
