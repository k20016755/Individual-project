import random
import sys
import pytest


def evenorodd(num):
    if not isinstance(num,int):
        raise TypeError("Please enter any number not a string")
        #num = int (input (""))
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

def test_ifnum():
    with pytest.raises(TypeError):
        evenorodd("9")
    #n = random.randint(0,10)
    #outcome = is_num(n)
    #assert outcome == False
#def multiply(a,b):
  #  return a*b
#@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
#def test_multiply():
 #   assert multiply(2,3)==6

#@pytest.mark.xfail
#def test_assert(raises=AssertionError):
 #   assert True == False



