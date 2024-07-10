import logging

import pytest
import requests
from faker import Faker

logger = logging.getLogger('api')

URL = "https://restful-booker.herokuapp.com"


#gitfaker = Faker()

def pytest_addoption(parser):
    parser.addoption("--api-url", action="store", default="https://restful-booker.herokuapp.com", help="URL для "
                                                                                                            "API")



@pytest.fixture(scope='session')
def url(request):
    url = request.config.getoption("--api-url")
    logger.info(f'Start tests, url is {url}')
    return url

#@pytest.fixture
#def create() -> dict:
#body = {"firstname": faker.first_name(), "lastname": faker.last_name(), "totalprice": , "depositpaid": , ""}
#response = requests.post(url=f'{URL}/booking', json=body)
#assert response.status_code == 200
#return body
