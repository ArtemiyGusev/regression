import os
from regression.utils.requests_helper import BaseSession


def reqres() -> BaseSession:
    reqres_url = os.getenv('reqres')
    return BaseSession(base_url=reqres_url)