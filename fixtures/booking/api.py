from common.requests_logger import requests_logger
#from fixtures.booking.schema import CREATE_SCHEMA
from fixtures.http_client import Client


class Create:
    def __init__(self, url):
        self.client = Client()
        self.url = url

    _POST_CREATE = 'booking'

    def create(self, body: dict,):
        res = self.client.request('POST',
                                  f'{self.url}/{self._POST_CREATE}',
                                  json=body)
        #schema.validate(res.json())
        requests_logger(res)
        return res
