# DAY-3 of Language Training in Python

# Data Structures and Algorithms

array1=[1,"one",2,"Two",3.14,]
print(type(array1))
print(len(array1))
print(array1[1])
print("___________________")
cars=["Tata",
      "Mahindra",
      "Maruti Suzuki",
      "Honda",
      "Hyndai",
      "Kia",
      "BMW",
      "Audi",
      "Skoda",
      "Mercedes Benz",
      "Jaguar",
      "Land Rover",]
cars.append("Volkswagen")
cars.append("Mini")
cars.pop(1) 
cars.reverse()
cars.sort()
# To access elements of array, we can use a FOR IN loop or Iterators

for i in cars:
    print(i)

# Linked List
def Linked_List():
    print("______________________Linked List___________________________")

    
    

    
def stack():
    print("________________________Stack_______________________________")

    stack1=[] 
    def push(stack1,value):
        stack1.append(value)
    def pop(stack1):
        stack1.pop()
    def top(stack1):
        print(stack1[len(stack1)-1])
    def display(stack1):
        for i in stack1:
            print(i)

    print("Enter Start to Continue? ")
    start_or_exit=str(input("Enter Choice:- "))
    while start_or_exit.lower()=="start":
        print("Choose Operation :- \"PUSH\" , \"POP\", \"PRINT\" ,\"TOP\" OR \"EXIT\"")
        choice1=str(input("Enter Choice Here:- "))
        if choice1.lower()=='exit':
            start_or_exit="exit"
        elif choice1.lower()=="push":
            value=input("Enter Value:- ")
            push(stack1,value)
        elif choice1.lower()=="pop":
            pop(stack1)
        elif choice1.lower()=='top':
            top(stack1)
        elif choice1.lower()=="print":
            display(stack1)

def queue():
    print("________________________Queue_______________________________")

    queue1=[] 
    def enqueue(queue1,value):
        queue1.append(value)
    def dequeue(queue1):
        queue1.pop(0)
    def front(queue1):
        print(queue1[len(queue1)-1])
    def display(queue1):
        for i in queue1:
            print(i)
    def rear(queue1):
        print(queue1[0])

    print("Enter Start to Continue? ")
    start_or_exit1=str(input("Enter Choice:- "))
    while start_or_exit1.lower()=="start":
        print("Choose Operation :- \"ENQUEUE\" , \"DEQUEUE\", \"PRINT\" ,\"FRONT\" , \"REAR\" OR \"EXIT\"")
        choice2=str(input("Enter Choice Here:- "))
        if choice2.lower()=='exit':
            start_or_exit1="exit"
        elif choice2.lower()=="enqueue":
            value=input("Enter Value:- ")
            enqueue(queue1,value)
        elif choice2.lower()=="dequeue":
            dequeue(queue1)
        elif choice2.lower()=='front':
            front(queue1)
        elif choice2.lower()=="print":
            display(queue1)
        elif choice2.lower()=='rear':
            rear(queue1)


"""DEQUEUE:- It means Doubble ended Queue, Which as the name suggests has two ends for 
    Enqueue and Dequeue based on the varient:- it has two varients :-

    OUTPUT RESTRICTED QUEUE:- In which Deletion can only be performed on Any one end of queue end
    While Insertion can be performed on both the ends
    
    INPUT RESTRICTED QUEUE:- In which Insertion can only be performed on any one of Queue end 
    While Deletion can be performed on both the ends"""


# _________HASH TABLE or Dictionary for Python____________
dict1={"Name":"ish" ,
       "Company":"CubexO" ,
       "Role":"Associate Software Engineer" ,
       "Age":21 ,
       "Default" : "" ,

       }

print(hash(dict1["Name"]))
print(hash(dict1["Age"]))
print(hash(dict1['Company']))

list1=[1,"One"]
print(hash(list[0]))
print(hash(list[1]))

print(dict1.items()) #Prints all the items present in the Dictionary
# dict1=dict1.setdefault("","This is By setdefault Function")
# print(dict1)

print(dict1.values())

del dict1['Name']
print(dict1)


# __________Recursion___________
'''Recursion is a Process in which a function calls itself again and again untill a base condition is met 
   or A process is called again and again untill the condition is satisfied'''

# Program to print the fibonacci series upto n_terms

# Recursive function
def fibonacci_series(value):
    if value <= 1:
        return value
    else:
        return(fibonacci_series(value-1) + fibonacci_series(value-2))

value=int(input("Enter How many Fibonacci Numbers You Want:- "))
fibonacci=[]
if value <= 0:
    print("Enter Positive Value")
else:
    print("Fibonacci series till",value,"Is:- ")
for i in range(value):
	fibonacci.append(fibonacci_series(i))

for i in fibonacci:
    print(i)

print("_________________________________________________")

def binary_search(list,k):
    list2.sort()
    print("The Given List is:- ")
    for i in list2:
        print(i,end=" ")
    right=0
    
    left=len(list2)-1
    while right<=left:
        mid=int((right+left)/2)
        if list2[mid]==k:
            print("\nYes,",k,"Is Present at:- ",mid)
            break
        elif int(list[mid]) > k:
            left=mid-1
        elif int(list[mid]) < k:
            right=mid+1
    print("\n",k,"Not Found in Given List!!")
list2=[1,0,2,9,3,8,4,7,5,6]
binary_search(list2,30)

'''BST is abbreviation of Binary Search Tree:- Its a Data Structure formed with root and nodes with exactly two
   nodes, One on Right, One on Left, the node on  the left should always be less than the root node and the one the right 
   should always be greater than the Root node'''
"""By this way retrieveing data is brought down to O(log(n)) time complexity"""

# ________________________Sorting Algorithms______________________

# Bubble Sort Algorithm:- It Compares Two Adjacent Values and 
#Swaps them if needed to make the list Sorted in Ascending Order

def BubbleSort(list3):
    for i in range(0,len(list3)):
        for j in range(0,len(list3)-1):
            if list3[j]>=list3[j+1]:
                list3[j],list3[j+1]=list3[j+1],list3[j]
list3=[9,1,8,2,3,1,4,]
BubbleSort(list3)

for i in list3:
    print(i,end=" ")