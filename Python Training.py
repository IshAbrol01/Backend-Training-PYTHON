print("Greetings, Welcome to My Python Language Learing Journey")
# Python Language Training 
                                # DAY-1 Learn The Basics
                                # Understanding Python Basic Syntax 
print("Hello and Welcome to CubexO")
a=5
b="Python Uses Interpreter unlike Compiler Used by Other Programming Languages"
if(a>4.5):
    print(b)
else:
    print("Python is Dynamically Typed Language")

"""a1="Indentation Plays a very Crucial Role is Python Programming"""
a=5
print("a is:-",a," & is of type:-",type(a))
a="5"
print("a now is:- ",a,"and is of type:- ",type(a))

# Explicit Type Casting
a=int(5)
a=float(a)
print(a," ",type(a))

                                #Python Variables
# 91a="Not Possible"
_a="Possible"
# -a="Not Possible"
a91="Possible"
A="Possible"
_Aa="Possible"

a,b,c=1,2,3
print(a,b,c)
x=y=z="CubexO"
print(x,y,z)

                                # Data Types
def typeo(x):
    print(type(x))
x="Hello Cubexo"
typeo(x)
x=1
typeo(x)
x=3.14
typeo(x)
x=3j
typeo(x)
x=["hi","This","is","a","LIST",1,2,3,4]
typeo(x)
x={"hi","This","is","a","LIST",1,2,3,4}
typeo(x)
x=("Hi",1,"There")
typeo(x)
x={"key":"value",1:"One"}
typeo(x)
x=False
typeo(x)

                    #Conditionals 
x=5
if(x==4):
    print("Its FOUR")
  
elif(x==3):
    print("Its Three")

else:
    print("Its neither 3 nor 4")

a=int(4)
b=str("4")
if(a==b):
    print("True")
elif(a!=b):
    print("not equal")
elif(a<b):
    print("Less Than")
elif(a<=b):
    print("Less than or equal to")
elif(a>b):
    print("Greater Than")
else:
    print("Greater than or equal to")

if(a==b and a!=4):
    print("Test")
elif(a==b or b==4):
    print("Test2")

                        #Type Casting and Exceptions
x=int(1)
y=float(x)
print(y)
z=str(x)
z1=int(z)
print(z1)
a=1
b=2.0
c=a+b
print(c,type(c))  #Implicit Type Casting
# a="5"
# b="t"
# n=int(a)
# print(type(n))
# n=int(b)
# print(n)
# print(type(n))

"""The Above Expression results in an ERROR since Char 't' cannot be converted to int directly, 
it can be converted to its ascii value though"""

                            #Functions
def Cubexo():
    print("Hello to the amazing world of Coding")
# Calling the function
def Calculator(a,b,c,operation):
    if(operation=="+"):
        c=a+b
    elif(operation=="-"):
        c=a-b
    elif(operation=="*"):
        c=a*b
    elif(operation=="-"):
        c=a/b
    else:
        print("Invalid Operation Requested")
        return
    print(a,operation,b,"=",c)
    
Cubexo()
print("Valid Operations:-'+','-'.'*','/' ")
a=int(input("Enter A:- "))
b=int(input("Enter B:- "))
c=0
operation=str(input("Enter Operation:- "))
Calculator(a,b,c,operation)

# *args is known as Arbitary Argument:- Used when we dont know exact number of Arguments that are going 
# to be passed to the given function.
def Demo1(*words):
    print(words[3])

Demo1("Hi","There","Welcome","To","CubexO")

# Keyword Arguments aka Kwargs:- consist of key = value syntax, 
# that means best_company = "CubexO" &  other_compnay = "Dosen't Matter"
# Here the sequence of sedning wont matter 

def award_ceremony(other_company,best_company):
    print("And The Award for Best Software Consultancy Firm Goes to:- ",best_company)

award_ceremony(best_company="CubexO",other_company="Dosen't matter")


# Arbitary Keyword Arguments aka **kwargs
# If number of Keyword Arguments is unknown

def test_func(**company):
    print("The Best Organisation:- " + company["winner"])

test_func(runner="Dosent matter", winner="CubexO")

# Default Parameter:- If no argument is given to function, defalut value is used def name(arg1="value")

                                # Built-In Functions


                            #   List
list1=[1,2,3,4,"One","Two","Three","Four",True,False,1.1]
for x in list1:
    print(x)
print(type(list1))
#                              Tuple
tuple1=(1,2,3,4,"One",True,1.1)
for x in range(0,len(tuple1)):
    print(tuple1[x])
print(type(tuple1))

# Set
set1={1,2,3,4,"5","Six",1,2,3,4}
for x in set1:
    print(x)
print(type(set1))

# Dictionary

dict1={"Name":"Ish",
       "Surname":"Abrol",
       "Company":"CubexO",
       "Designation":"Associate Software Developer"}
print(dict1)

# ______________________________________________________________________________________________

                            # Questions For Review

# Basic Data Types in Python
int1=1
str1="String"
float1=1.1
complex1=3j
list1=[1,2,"Three"]
tuple1=(1,2,"four",1,2)
set1={1,1,1,1,1,1}
dictionary1={"name":"Ish",1:"One"}

# Type Conversion
a=1
b=2
c=float(a+b)
print(c,type(c),type(a))
d=str(c)
print(c,type(c))


# Conitionals


name = "Ish"
Leave_Count = 3
if(name=="Ish" and Leave_Count>=5):
    print("Ruk tera toh game bajana padega, Khopdi Tod saale ka")

elif(name=="Ish" and Leave_Count<4):
    print("Me toh tereko rakshas samjha re, par tu toh dev manus nikla re")


# Exception Handling
def test_function1(a,b,c):
    b=10
    c=a+b
    return c

def test_function2(a,b,c):
    c=a/b
    return c
try:
    a=10
    b=0
    
    test_function1(a,b,c)
    test_function2(a,b,c)
except ZeroDivisionError:
    print("Bawa 0 se kuch Divide Hota hai kya, Ayeeeeeeeeeeeee")

# Defining Function with Default Parameters

def demo_default(a=0,b=0):
    ans=a+b
    print(ans)
demo_default(2,3)
demo_default()

# List Comprehension

list1=[]
for i in range(1,11):
    list1.append(i*i)
print(list1)

# Major Difference between LIST & TUPLE is that
# List is Mutable, i.e. its content can be altered [] 
# TUPLE is immutabel i.e. its content cannot be changed once set ()

# Set operations

set11={1,1,2,2,3,3,4,4,"Five","Five"}
set11.add("Six")
set11.remove(4)
set11.discard(3)

print(set11)



    