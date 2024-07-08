import requests


class Client:
    @staticmethod
    def request(method, url, **kwargs):
        return requests.request(method, url, **kwargs)