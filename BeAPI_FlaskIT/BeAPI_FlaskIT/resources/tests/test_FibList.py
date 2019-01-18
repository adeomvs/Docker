import pytest
from flaskit.pytest import execute_endpoint


def test_endpoint_FibList():
    code, body = execute_endpoint("FibList")
    assert code == 200
    assert "_metadata" in body