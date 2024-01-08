# Python Backend Training Day-4 + Tasks
# Testing 
# DOCTEST:- As the name suggest, DocTest allows to Document and Run Test Case from Python's Docstring itself
# MAJOR DIFFERENCE BETWEN DOCSTRING(""" or ''') AND COMMENT(#) is that DocStrings are not IGNORED by Interpreter, 
# hence they are a living part of code.
"""This is A Docstring"""
'''This is Also a Docstring'''
# This is a COMMENT and is completely Ignored by Interpreter
'''There are two types of tests :- Acceptance test(Tests used to determine if specification of given product are met) 
and Integration Test (Tests done to ensure that different components of a project work correctly as a group)'''
 


def add(a, b):
    """
    >>> add(5, 5)
    10.0
    >>> add(0,0)
    0
    """
    return float(a+b)

def factorial(x):
    """
    >>> factorial(5)
    120
    >>> factorial(10)
    3628800
    """
    result=1
    for i in range(1,x+1):
        result=result*i
    return result

def print_check(name="Anonymous User"):
    """
    >>> print_check("Ish")
    Hello Ish How are you Doing?
    >>> print_check()
    Hello Anonymous User How are you Doing?
    """
    print(f"Hello {name} How are you Doing?")
    
# Command To check and run all test cases is :- python3 -m doctest -v "file name"
# the line right next to >>> is the expected output of that function with the given values, If matched, it gives OK
    
def failing_testcase(self):
    """
    >>> failing_testcase():

    """
    print()

def division(a,b):

    """
    >>> division(10,5)
    2.0
    >>> division(1,0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    >>> division(0,0)
    0.0
    """

    return float(a/b)

# UNITTEST 
# Test Fixture :- Arrangements that act as a baseline to ensure that the test results are accurate and Repeatable.
# Test Case :- A demo enviornment created to test how code snippet will work under the given conditions.
# Test Suit :- A collection of Test Cases and Enviornment to test the given code snippet to 
#check its behaviour in a particular enviornment with all possible scenarios
# Test Runner :- A test runner is a component that executes tests and check for output


import unittest

class UT(unittest.TestCase):
    def TestUpper(self):
        self.assertEqual('CubexO'.upper(),'CUBEXO')

    def TestSplit(self):
        a="CubexO Software Solutions"
        self.assertEqual(a.split(),['CubexO','Software','Solutions'])
    
if __name__ == '__main__':
    unittest.main()


# PyTest
# Highly Readble and Simplistic Testing Tool


    
# test_assert_examples.py

def test_uppercase():
    assert "CuBeXo".upper() == "CUBEXO"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        
    }
    print("EOD")