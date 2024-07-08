import logging

import pytest
import requests
from faker import Faker

logger = logging.getLogger('api')

URL = "https://restful-booker.herokuapp.com/auth"


#faker = Faker()

def pytest_addoption(parser):
    parser.addoption("--api-url", action="store", default="https://restful-booker.herokuapp.com/auth", help="URL для "
                                                                                                            "API")
#def pytest_addoption(parser):
    #parser.addoption( action="store", default='https://restful-booker.herokuapp.com/auth',
                     #help="API url")


@pytest.fixture(scope='session')
def url(request):
    url = request.config.getoption("--api-url")
    logger.info(f'Start tests, url is {url}')
    return url

#@pytest.fixture
#def regsiter() -> dict:
#body = {"username": faker.email(), "password": faker.password()}
#response = requests.post(url=f'{URL}/register', json=body)
#assert response.status_code == 201
#return body
