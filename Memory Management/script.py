import sys


# _____________INTEGER______________

'''an empty Interger Data type will hold a space of 24 bytes and then 28 bytes of space will be occupied by 
   it from values ranging from 0 to 999999999 [9 digits] and a further addition of 4 bytes after every 10 digits addition'''


# ___________FLOAT__________________

a=float()
b=0.0
c=1
d=1.0
e=1.123456789
f=1.1234567890
g=100.12345678901234567890
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(sys.getsizeof(c))
# print(sys.getsizeof(d))
# print(sys.getsizeof(e))
# print(sys.getsizeof(f))
# print(sys.getsizeof(g))


#____________string_______________
# Empty string takes up 49 Bytes and then every subsequest character takes up 1 byte 
# i.e. a="" will have 49 bytes 
# and a="a" will take 50 bytes
string1=""
# print(sys.getsizeof(string1))
string2="1"
string3="A"
string4="a"
string5="AaBb01"
string6="abcdefghijklmnopqrstuvwxyz1234567890"
# print(sys.getsizeof(string2))
# print(sys.getsizeof(string3))
# print(sys.getsizeof(string4))
# print(sys.getsizeof(string5))
# print(sys.getsizeof(string6))


# __________LIST___________

list1=[]
list2=[1,]
list3=[1]
list4=[1,2,3]
list5=["a","b","c"]
list5=['a','b','c']
list6=["aaa","bbb","ccc"]
list7=[1234567890,1234567890,1234567890]
list8=[1,2,3,4,5,6,7,8,9,0]

# print(sys.getsizeof(list1))
# print(sys.getsizeof(list2))
# print(sys.getsizeof(list3))
# print(sys.getsizeof(list4))
# print(sys.getsizeof(list5))
# print(sys.getsizeof(list6))
# print(sys.getsizeof(list7))
# print(sys.getsizeof(list8))


# list11=[]
# print("Size of Empty List is:- ",sys.getsizeof(list11))
# for i in range(55):
#     print("Size of list is:- ",sys.getsizeof(list11))
#     list11.append(i)


# ____________TUPLE___________________

tuple1=()
tuple2=(1)
tuple3=(1,2)
tuple4=(1,2,3,4,5)
tuple5=("aa","bb","cc","dd","ee")
tuple6=("a")
tuple7=('a')

# print(type(tuple1),sys.getsizeof(tuple1))
# print(type(tuple2),sys.getsizeof(tuple2))
# print(type(tuple3),sys.getsizeof(tuple3))
# print(type(tuple4),sys.getsizeof(tuple4))
# print(type(tuple5),sys.getsizeof(tuple5))
# print(type(tuple6),sys.getsizeof(tuple6))
# print(type(tuple7),sys.getsizeof(tuple7))


# ____________SET__________________

set1=set({})
set2={1}
set3={1,2,}
set4={1,2,3,}
set5={1,2,3,4,}
set6={1,2,3,4,5,}
set7={1,2,3,4,5,6,}
set8={1,2,3,4,5,6,7,}
set9={1,2,3,4,5,6,7,8,}
set9={1,2,3,4,5,6,7,8,9,}
set10={1,2,3,4,5,6,7,8,9,10,}

# print("1",type(set1),sys.getsizeof(set1))
# print("2",type(set2),sys.getsizeof(set2))
# print("3",type(set3),sys.getsizeof(set3))
# print("4",type(set4),sys.getsizeof(set4))
# print("5",type(set5),sys.getsizeof(set5))
# print("6",type(set6),sys.getsizeof(set6))
# print("7",type(set7),sys.getsizeof(set7))
# print("8",type(set8),sys.getsizeof(set8))
# print("9",type(set9),sys.getsizeof(set9))
# print("10",type(set10),sys.getsizeof(set10))
# set5.add(0)
# print(type(set5),sys.getsizeof(set5))
# set11=set({})
# for i in range(1,11):
#     print("size of set with",len(set11),"elements is",sys.getsizeof(set11))
#     set11.add(i)


# for i in set11:
#     print(i,end=" ")

# print()

# for i in set10:
#     print(i,end=" ")


# ______________DICTIONARY____________

abc=dict({})
print(type(abc),"Size:- ",sys.getsizeof(abc))
# for i in range(1,11):
#     dict[i]=i









