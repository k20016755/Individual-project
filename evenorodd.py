#example.py



import unittest
import random

class BankAccount:
  def __init__(self, id):
    self.bankid = id
    self.balance = 0

  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance -= amount
      return True
    return False

  def deposit(self, amount):
    self.balance += amount
    return True


   
class TestBankOperations(unittest.TestCase):
    def test_low_deposit(self):
      a = BankAccount(1)
      a.deposit(100)
      outcome = a.withdraw(200)
      self.assertFalse(outcome)
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
        self.assertIsNone(n)
    def test_ifnum(self):
        n = random.randint(0,10)
        evenorodd.check(n)


if __name__ == '__main__' :
  unittest.main()