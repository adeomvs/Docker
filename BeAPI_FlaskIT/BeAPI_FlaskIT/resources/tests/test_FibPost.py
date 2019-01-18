import pytest
from flaskit.pytest import execute_endpoint

@pytest.mark.parametrize("n, fibN", [
        (0, 0),
        (1, 1),
        (-1, 0),
        (3, 2)
])

def test_endpoint_FibPost(n, fibN):
    query = {
        "n": n,
    }
    code, body = execute_endpoint("FibPost", query=query)
    assert code == 201
    assert body["item"]["fibN"] == fibN
