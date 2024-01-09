# <<<<<<< Day-4Python
# PyTest and UnitTest Remedial

import unittest
import math
import pytest

@pytest.fixture
def input_string():
    string="CuBeXo"
    return string


@pytest.mark.always
def test_always_pass():
    assert True


@pytest.mark.always
def test_always_fails():
    assert False


@pytest.mark.case
def test_checkUppercase(input_string):
    # string="CubExO"
    assert input_string.upper() == 'CUbEXO'


@pytest.mark.case
def test_checklowerCase(input_string):
    # string="CUBExO"
    assert input_string.lower() == 'cubexo'


@pytest.mark.square
def test_checkSqr():
    assert math.sqrt(49) == 7


# @pytest.mark.email
# def test_email():
#     string="ish.abrol@cubexo.io"
#     assert

# Parameterizing Test 
#   :-  Parameterizing of a test is done to test the code snippet against 
#       multiple input to check for its robustness and scalability
    
@pytest.mark.parametrize("num",[2,4,10,30,6])
@pytest.mark.even
def test_isEven(num):
    assert  num%2==0


# Xfail and Skip
    """
    Xfail:- command(@pytest.mark.xfail) if the function is marked with this,
    that code snippet will not be considered for any testing, usually a code snippet is marked with it when we have
    code under development: -here the pytest wont raise any error irrespective of the code passing test case or not

    skip :- command(@pytest.mark.skip) if the snippet is marked with this, al the tests are skipped that were ought to
    that particular code snippet.

    DIFFERENCE :- function marked with Xfail will still has all the test performed on it but the result(pass/fail)
    wont have any effect 
    while
    function marked with skip will have no test performed on it
    """


    # --maxfail :- runs on terminal, takes integer input value 
    # "It determines that the following test procedures to stop after 'n' failed test" 
    # Command :- pytest maxfail <int value>

    # RUN TEST in PARALLEL command :- "pytest -n <int value>"

    '''
    Print Test Result in XMl format
    command :- file_name.py -v --junitxml="result_file_name.xml"

    '''

    # to run a specific functio of test we use command :- pytest -k <test_function_name>
# =======
# >>>>>>> main
