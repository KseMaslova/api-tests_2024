from common.requests_logger import requests_logger
from fixtures.http_client import Client


class Create:
    def __init__(self, url):
        self.client = Client()
        self.url = url

    _POST_CREATE = 'booking'

    def create_booking(self, body: dict):
        res = self.client.request('POST',
                                  f'{self.url}/{self._POST_CREATE}',
                                  json=body)
        requests_logger(res)
        return res


class Get:
    def __init__(self, url):
        self.client = Client()
        self.url = url

    def get_booking(self, id, body=None):
        res = self.client.request('GET',
                                  f'{self.url}/{id}',
                                  json=body)
        requests_logger(res)
        return res
