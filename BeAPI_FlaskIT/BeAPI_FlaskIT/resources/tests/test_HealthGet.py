import pytest
from flaskit.pytest import execute_endpoint


def test_endpoint_HealthGet():
    code, body = execute_endpoint("HealthGet")
    assert code == 200
    assert body["_metadata"]["status"] == 0