import pytest

from  bissextile_case import Multiples

def test_raises_exception_on_string_arguments():
    with pytest.raises(TypeError):
        Multiples("toto")

def test_multiples5():
    assert Multiples(5) == False

def test_multiples4():
    assert Multiples(8) == True

def test_multiples6():
    assert Multiples(200) == False

def test_multiples7():
    assert Multiples(400) == True

def test_multiples8():
    assert Multiples(2004) == True

def test_multiples1():
    assert Multiples(4) == True

def test_multiples2():
    assert Multiples(104) == True

def test_multiples3():
    assert Multiples(300) == False
