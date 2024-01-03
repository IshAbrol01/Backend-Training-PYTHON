print("Language Training DAY-1 Revision Script")
# Understanding Basic Python Syntax
for i in range(1,11):
    print(i)
    
'''Multi-Line Comments'''
"""This Too"""
j=11
while j<21:
    print(j)
    j+=1

age=21
if age==20:
    print("ek Saal aur")
elif age >=21:
    print("Eligible")
else:
    print("Not Eligible")

a=5
print(type(a))
a="5"
print(type(a))
a=5.0
print(type(a))

# Built-In Data Structures
# list
list1=[1,2,3,4,5]
print(type(list1))
list1.append("5")
list1.append("Six")

# list2=list(list1.copy())
list2=["seven","Eight"]
# for i in list2:
#     print(i)


print(list1.count(5))
print("__________________")

list1.extend(list2)

print("The Index of \"SIX\" is:- " ,list1.index("Six"))

list1.insert(0,"Zero")
list1.pop() #Removes last element from list
list1.remove("5")  #Removes the exact mentioned value from the given list

list1.reverse()
print("Index of\"Seven\" is:- ",list1.index("seven"))
list3=[2,5,5,1,2,6,8,3,1,2,5,61,1,5,1]
list3.sort()
for i in list3:
    print(i," ")
for i in list1:
    print(i)

# ____________________LIST COMPREHENSION_________________
#  
square=[i*i for i in range(1,11)]
double=[i*2 for i in range(1,11)]


for i in square:
    print(i," ")

# TUPLE
    
tuple1=(1,2,3,4,5,6,7,8,9,10)
print(type(tuple1))

print(tuple1.count(2))
print(tuple1.index(1))
# tuple1.append("ZERO") Since tuple is IMMUTABLE, we canot insert anythin or delete any of its content

# SET
print("____________________________")
set1={1,2,3,3,3,4,5,5,6,7,8,8}
set2={1,2,3,4,5}
set1.add(9)
print("Difference between set1 and set2 is:- ",set1.difference(set2))

set1.pop()
for i in set1:
    print(i)


#Dictionary___________________________________________________
dict1={"name":"Ish","Company":"CubexO","Role":"Associate Software Engineer Trainee","Age":20,"name":"Ish Abrol"}
dict1['full_name']="ISH ABROL"
dict1['name']="Ish Abrol 123"
print(dict1.get('Company'))
print(dict1.keys())
print(dict1.values())
x=('a','b','c')
y=(0)
dict3=dict.fromkeys(x,y)
print(dict3)
print("Here is Dict1 items ",dict1.items())
dict1.setdefault('',"Please ask for a valid Key")
print(dict1.get('give_default'))
# Dictionary Comprehension:- A Dictionary that has value : value square upto 10[for value]
dict2={x:x*x for x in range(1,11)}
print(dict2)



print(dict1)


# Regular Expression_________________________
import re
string1="ABCDEFGHAIJKLMNOPQRASTUVWXYZISHAISGREATaAbcdefAghijklAmnAopqrAstuvwAxyz"
pattern="ISH"
print(re.search("ISH",string1))
print(re.findall("A",string1))


    

    

