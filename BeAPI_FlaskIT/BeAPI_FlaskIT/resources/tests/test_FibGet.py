import pytest
from flaskit.pytest import execute_endpoint


@pytest.mark.parametrize("id", [(1), (2)])
def test_endpoint_FibGet(id):
    path_args = {"id": id}
    body = {}
    code, body = execute_endpoint("FibGet", path_args=path_args, body=body)
    assert code == 200
    assert "_metadata" in body