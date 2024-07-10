from common.requests_logger import requests_logger
from fixtures.http_client import Client


class Create:
    def __init__(self, url):
        self.client = Client()
        self.url = url

    _POST_CREATE = 'booking'

    def create(self, body: dict):
        res = self.client.request('POST',
                                  f'{self.url}/{self._POST_CREATE}',
                                  json=body)
        requests_logger(res)
        return res


class Get:
    def __init__(self, url):
        self.client = Client()
        self.url = url

    _POST_GET = 'booking/:id'

    def get(self, body=None):
        res = self.client.request('GET',
                                  self.url,
                                  json=body)
        requests_logger(res)
        return res
