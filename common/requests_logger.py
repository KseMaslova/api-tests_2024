import logging

from requests import Response

logger = logging.getLogger('api')


def except_no_content(response: Response):
    try:
        return response.request.body.decode('utf-8')
    except AttributeError:
        return 'no content in request'


def requests_logger(response: Response):
    # request
    logger.info(f"Request: url: {response.request.url}, "
                f"method: {response.request.method}, body: {except_no_content(response)}")
    # response
    logger.info(f"Response: status code: {response.status_code}, body: {response.json()}")
