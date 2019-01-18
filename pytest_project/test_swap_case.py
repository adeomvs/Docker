import pytest

from my_fonction import swap_case

def test_swap_case():
    assert swap_case('oBJECTIF-libre') == "Objectif-LIBRE"

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        swap_case(9)
