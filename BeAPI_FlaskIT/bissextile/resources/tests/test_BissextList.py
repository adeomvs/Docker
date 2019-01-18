import pytest
from flaskit.pytest import execute_endpoint


def test_endpoint_BissextList():
    code, body = execute_endpoint("BissextList")
    assert code == 200
    assert "_metadata" in body