# In This Code Snippet we will be writing some Random Functions and then Writing Test Cases in DOCTEST

# This is A comment, it is completely ignored by Interpreter
"""While This"""
'''& This is caled DocString, It is not Ignored by Interpreted and lets you to perform several Testing Here too'''


employee_list = [
    "ceo sir" ,
    "cto sir" ,
    "saharsh sir" ,
    "abhieshek sir" ,
    "avni ma'am" ,
    "artika ma'am" ,
    "abhishek sir" ,
    "surya sir" ,
    "ish abrol" ,
    "jay baldwa" ,
    "jiya solnaki" ,
    "krati sengar" ,
    "hiteshi ma'am"
    ]

search_query="Ceo Sir"

def is_employee(employee_list,search_query):
    """
    >>> is_employee(employee_list,"Kanak")
    No, Doesn't Work in this Organisation

    >>> is_employee(employee_list,"SaharSh SIr")
    Yes, Works Here!!

    >>> is_employee(employee_list,"CtO sIR")
    Yes, Works Here!!

    >>> is_employee(employee_list,4321)
    Traceback (most recent call last):
      File "/usr/lib/python3.10/doctest.py", line 1350, in __run
        exec(compile(example.source, filename, "single",
      File "<doctest Doctest.is_employee[3]>", line 1, in <module>
        is_employee(employee_list,4321)
      File "/home/my/Desktop/Python/Backend-Training-Python/TestCases/Doctest.py", line 43, in is_employee
        if search_query.lower() in employee_list:
    AttributeError: 'int' object has no attribute 'lower'

    >>> is_employee(employee_list,"avni ma'am")
    Yes, Works Here!!


    """
    
    if search_query.lower() in employee_list:
        print("Yes, Works Here!!")
    else:
        print("No, Doesn't Work in this Organisation")

# is_employee(employee_list,search_query)
# is_employee(employee_list,"saharsh sir")
# is_employee(employee_list,"kanak poddar")


# def isLeapYear(*arg):
#     if ((arg%400 == 0) or 
#     (arg%100 != 0) and 
#     (arg%4 == 0)):
#       print("Leap Year")

#     else:
#         print("Not a Leap Year")

# isLeapYear(2024)

def isLeapYear1(*arg):
    '''
    >>> isLeapYear1(2025)
    Not a Leap Year

    >>> isLeapYear1(1947)
    Not a Leap Year

    >>> isLeapYear1(1945)
    Not a Leap Year

    >>> isLeapYear1(2024)
    Leap Year

    >>> isLeapYear1(0)
    Invalid Year Input Range:- 1 to Infinity'''

    arg1=arg[0]
    if arg1 <= 0:
        print("Invalid Year Input Range:- 1 to Infinity")
    elif ((arg1%400 == 0) or 
    (arg1%100 != 0) and 
    (arg1%4 == 0)):
      print("Leap Year")

    else:
        print("Not a Leap Year")


def isValidEmail(*args):
    """
    >>> isValidEmail("ish.abrol@cubexo.io")
    Valid Email Entered

    >>> isValidEmail("ish.@gmail.com")
    Valid Email Entered

    >>> isValidEmail("1234@gmail.com")
    Valid Email Entered

    >>> isValidEmail(".ish@cubexo.IO")
    Valid Email Entered

    >>> isValidEmail("ish@.com")
    Invalid Email

    >>> isValidEmail("ish@cubexo.")
    Invalid Email
    """
    flag=0
    args2=str(args[0])
    at_the_rate_index=args2.find("@")
    if at_the_rate_index == 0:
        flag=1
    for i in range(0,len(args2)):
        if args2[i] == ".":
            dot_index=int(i)
    if dot_index == len(args2)-1:
        flag=1
    if ((dot_index - at_the_rate_index) <= 1):
        flag = 1
    if(flag == 1):
        print("Invalid Email")
    else:
        print("Valid Email Entered")

# isValidEmail("ish.abrol@cubexo.io")
# isValidEmail("ish.abrol@cubexo")
# isValidEmail("ishabrol04@gmail.com")
# isValidEmail("ish@.com")
# isValidEmail("ish@cubexo.")
# def test(self):
#     return 10,20,30
# x=test()
# a,b=10,20,30
# print(a)
# print(b)
