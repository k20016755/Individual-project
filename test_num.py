import random
import sys
import pytest
import coverage
cov = coverage.Coverage()
cov.start


def evenorodd(num):
    if not isinstance(num,int):
        raise TypeError("Please enter any number not a string")
        #num = int (input (""))
    if (num%2)==0:
        outstr="Even"
    else:
        outstr="Odd"
    return outstr


def test_ifnum():
    with pytest.raises(TypeError):
        evenorodd("9")
def test_if_even_ok():
    assert evenorodd(80) == "Even"
def test_if_0_even_ok():
    assert evenorodd(0) == "Even"
def test_if_negative_ok():
    assert evenorodd(-2)== "Even"
def test_if_odd_ok():
    assert evenorodd(101) == "Odd"

#@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
cov.stop()
cov.save()

#@pytest.mark.xfail
#def test_assert(raises=AssertionError):
 #   assert True == False



