# This Code Snippet contains Several Functions and then those Functions are tested with relevant test cases to check them for 
# their Robestness , Scalability and Task Specificity using PYTEST module 
"""______________________________________________________________________________________________________"""
# def test1():
#     return "1",2,"Three"
# a1,a2=test1()
# print("Type of a1 is:- ",type(a1))
"""The Above code snippet generates error(too many values to Unpack) since it returns 3 values and 
   we have assigned onyl 2 variables to it , Although if we will assign same number of variables as 
   the function returns, each value is assigne a variable with respective data type and 
   if we only assign a single variable while the function return more than one value,
   all the values the function is going to return will form a tuple and will be assigned to the variable mentioned."""
def demo():
    return 10,20,30
x,y,z=demo()
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

a=10,20,30
print(a)
# print(b)
print(type(a))

x1=tuple(x2 for x2 in range(0,11))
print(x1)
print(type(x1))

t1=([1,2,3],[4,5,6],[7,8,9])
print(type(t1))
for i in range(0,3):
    t1[0][i]=5
print(t1)
print(t1[0][1])



# _______________________________________PyTest___________________________________________

import pytest

def testAlwaysTrue(self):
    assert True
def testAlwaysFalse(self):
    assert False


def isValidContactNumber(*args):
    if len(args)<12 or len(args)>12:
        return "Invalid Contact Number"
    elif args[2] == 0:
        return "Invalid Contact Number"
    elif (args[0] != 9) and (args[1] != 1):
        return "Invalid Contact Number"
    else:
        return "Valid Contact Number"
@pytest.fixture
def checkInventory(**kwargs):
    
    for key, value in kwargs.items():
        if key == "quantity":
            if kwargs["quantity"] == 0:
                return "Ooff, This Product is Out Of Stock"
            elif (kwargs["quantity"] >= 1) and (kwargs["quantity"] <= 10):
                return "Hurry Up! only a Few Pieces left"
                # assert "Hurry Up! only a Few Pieces left"
            else:
                return "Order Now, Special Discounted Rate just for you"
            
# 1,99,100, 
# 1001



# 100 - 1000 1
# 1001- 2000 2
# 2001- 3000 3

def testcheck_inventory_max_order():
    test1=checkInventory(quanity=10000)
    assert test1 == "Order Now, Special Discounted Rate just for you"


    


# print(checkInventory(quantity=0))
# print(checkInventory(quantity=10))
# print(checkInventory(quantity=90))
# print(checkInventory(quantity=9))
# print(checkInventory(quantity=1))

    



