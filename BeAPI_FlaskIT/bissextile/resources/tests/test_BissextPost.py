import pytest
from flaskit.pytest import execute_endpoint

@pytest.mark.parametrize("year, expected_result", [
        (1600, True),
        (2100, False),
        (2004, True),
        (2013, False)
])

def test_endpoint_BissextPost(year, expected_result):
    query = {
        "Years": year,
    }
    code, body = execute_endpoint("BissextPost", query=query)
    assert code == 201
    assert body["item"]["isBissext"] == expected_result
