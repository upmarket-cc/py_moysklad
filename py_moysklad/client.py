from functools import cached_property

from py_moysklad.exceptions import NoCredentialsException
from py_moysklad.http import HTTP


class ApiClient:
    def __init__(self, token: str, host: str = "online.moysklad.ru"):
        self.host = host
        self.token = token

    @cached_property
    def http(self):
        if not self.token:
            raise NoCredentialsException(
                "Для работы требуется токен",
            )
        return HTTP(token=self.token, host=self.host)
