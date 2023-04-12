
import unittest
import random

class evenorodd:
    def check(num):
        if (num%2)==0:
            print ("Number is even")
        else:
            print("Number is odd")

    
class testevenodd(unittest.TestCase):
    def test_check(self):
        n = random.randint(0,10)
        evenorodd.check(n)
        self.assertIsNotNone(n)
    def test_ifnum(self):
        n = random.randint(0,10)
        evenorodd.check(n)


if __name__ == '__main__' :
  unittest.main()