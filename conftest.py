import logging

import pytest

logger = logging.getLogger('api')


def pytest_addoption(parser):
    parser.addoption("--api-url", action="store", default="https://restful-booker.herokuapp.com", help="URL для "
                                                                                                       "API")


@pytest.fixture(scope='session')
def url(request):
    url = request.config.getoption("--api-url")
    logger.info(f'Start tests, url is {url}')
    return url
