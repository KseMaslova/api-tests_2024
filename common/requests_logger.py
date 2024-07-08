import logging

from requests import Response

logger = logging.getLogger('api')


def requests_logger(response: Response):
    # request
    logger.info(f"Request: url: {response.request.url}, "
                f"method: {response.request.method}, body: {response.request.body.decode('utf-8')}")
    # response
    logger.info(f"Response: status code: {response.status_code}, body: {response.json()}")
