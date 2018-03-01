# from Factorial import *

import Factorial

subject=Factorial

# def test1():
#   assert subject.factorial(0) == 1
#
# def test2():
#   assert subject.factorial(1) == 1
#
# def test3():
#   assert subject.factorial(2) == 2
#
# def test4():
#   assert subject.factorial(3) == 6
#
# def test5():
#   assert subject.factorial(4) == 24
#
# def test6():
#   assert subject.factorial(5) == 120

class FactorialTest(object):
  def test1(self):
    assert subject.factorial(0) == 1, "assert 1 == 2 "  #"value was different to 1"

  def test2(self):
    assert subject.factorial(1) == 2, "assert 1 == 2, you should use n minus 1 as base case"

  def test3(self):
    assert subject.factorial(2) == 2

  def test4(self):
    assert subject.factorial(3) == 6

  def test5(self):
    assert subject.factorial(4) == 24, "assert 4 == 24"

  def test6(self):
    assert subject.factorial(5) == 120