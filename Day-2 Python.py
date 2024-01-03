# Decorator
# Nested Function

def outer(x):
    def inner(y):
        return x+y
    return inner

addition1=outer(1)
result=addition1(1)
print(result)

# Pass Function as an Argument

def addition2(x,y):
    return x+y
def anotherone(func,x,y):
    return func(x,y)

result1=anotherone(addition2,2,2)
print(result1)

def decorator2(func):

    def inner():
        print("The Decorator")
        func()
    return inner

@decorator2
def ordinary():
    print("The Function which will be Decorated")

ordinary()  

#Iterators
my_list=[1,0,2,9,3,8,4,7,5,6]
myiter=iter(my_list)
# while(myiter):
#     print(next(myiter))

# Lambda Function
    
x=lambda a:a*a

print(x(10))

# generators :- works like a normal function but yields value whenever needed

def addition3(x,y):
    yield x+y

print(addition3(4,4))

# Object Oriented Programming 
"""Classes, Objects, Inheritance, Encapsulation, Polymorphism"""

import os
import math

print(os.getcwd())

# Questions for review

# REGULAR EXPRESSION
import re

string1="Hello and Welcome to CubexO - Quality Code Studio"
pattern="CubexO"

print(re.findall(pattern,string1))

# def decorator3(func):
#     def times_function(a1,b1):
#         print(a1*b1)
#         func()
#     return times_function

# @decorator3
# def ordinary1(a1,b1):
#     print(a1*b1)


# ordinary1(1,1)

x=[(1,2,3),(2,1,3),(2,3,1)]
y=sorted(x,key=lambda x: x[1]) 
for i in y:
    print(i)
list2=[1,2,3,3,]
list4=[1,2,3,3]
print(len(list2))
print(len(list4))
