from common.requests_logger import requests_logger
from fixtures.auth.shema import AUTH_SCHEMA
from fixtures.http_client import Client


class Auth:
    def __init__(self, url):
        self.client = Client()
        self.url = url

    def auth(self, body: dict, schema=AUTH_SCHEMA):
        res = self.client.request('POST',
                                  f'{self.url}',
                                  json=body)
        schema.validate(res.json())
        requests_logger(res)
        return res
