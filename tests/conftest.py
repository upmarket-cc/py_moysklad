import json
from os import path

import pytest
from apiclient.request_strategies import BaseRequestStrategy

from py_moysklad.client import ApiClient


@pytest.fixture()
def read_fixture():
    """Fixture reader"""

    def read_file(file_path):
        with open(path.join("tests/.fixtures/", file_path) + ".json") as fp:
            return json.load(fp)

    return read_file


@pytest.fixture()
def mock_http_client(mocker):
    return mocker.Mock(spec=BaseRequestStrategy)


@pytest.fixture()
def client(mock_http_client):
    client = ApiClient.create_with_bearer_token(token="token", host="localhost")
    client.client.set_request_strategy(mock_http_client)
    return client
