import pytest

from py_moysklad.client import ApiClient
from py_moysklad.exceptions import NoCredentialsException


@pytest.mark.parametrize(
    ('token', 'password', 'login'),
    [
        (None, 'passw0rd', 'login'),
        ('tok3n', None, 'login'),
        (None, None, 'login'),
        ('tok3n', 'passw0rd', None),
        (None, None, None),
    ],
)
def test_no_credentials(token, password, login):
    client = ApiClient(token=token, password=password, login=login)
    with pytest.raises(NoCredentialsException):
        client.http
