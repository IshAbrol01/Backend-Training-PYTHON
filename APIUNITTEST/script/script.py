import requests
import unittest
import os

# print(os.getcwd())

#ByDefault Python interpreter searches for file in same directory but by using the SYS module we can 
#make the interpreter to look for files in the directory path mentioned with ssys.path.insert('path)
import sys
sys.path.insert(1,'/home/my/Desktop/Python/Backend-Training-Python/APIUNITTEST') 

from Constants.constants import URL

# API = URL()
# print("Dummy API link is: -",API)
class dummy_API_Testing:

    def dummy_post(self):
        self.data=dict({"name":"test","salary":"123","age":"23"})
        self.result = requests.post(URL(),self.data)
        return str(self.result.status_code) #String <Response [406]>
    

    def dummy_get(self):
        self.result=requests.get('https://dummy.restapiexample.com/api/v1/employee/1')
        return self.result.status_code
    

    def dummy_status_code():
        result=requests.get('https://dummy.restapiexample.com/api/v1/employee/1')
        return result.status_code
    


class negative_testing:


    def dummy_false_status_code(self):
        self.result=requests.get('https://dummy.restapiexample.com/api/v1/employe')
        return self.result.status_code
    
    def dummy_false_post(self):
        self.result=requests.post(URL(),{'n':'o'})
        return self.result.status_code
    
    def dummy_false_put(self):
        self.result=requests.put('https://dummy.restapiexample.com/public/api/v1/21',{"name":"test","salary":"123","age":"23"})
        return self.result.status_code



# obj1=dummy_API_Testing()

# print("-",obj1.dummy_post(),"-")
# print(type(obj1.dummy_post()))

# print(obj1.dummy_get())
# print(type(obj1.dummy_get()))

# print(obj1.dummy_status_code())
# print(type(obj1.dummy_status_code()))
    


# obj2=negative_testing()

# print(obj2.dummy_false_status_code())
# print(type(obj2.dummy_false_status_code()))

# print(obj2.dummy_false_post())
# print(type(obj2.dummy_false_post()))

# print(obj2.dummy_false_put())
# print(type(obj2.dummy_false_put()))