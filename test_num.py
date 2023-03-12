import random
import sys
import pytest

class evenorodd:
    def check(num):
        #num = int (input ("Please enter any number"))
        if (num%2)==0:
            print ("Number is even")

        else:
            print("Number is odd")
def is_num(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
def test_ifnum():
    n = random.randint(0,10)
    outcome = is_num(n)
    assert outcome == False
def multiply(a,b):
    return a*b
def test_multiply():
    assert multiply(2,3)==6

@pytest.mark.xfail
def test_assert(raises=AssertionError):
    assert True == False
