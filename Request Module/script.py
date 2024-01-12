import requests
import pytest
# x=requests.get("https://w3schools.com/python/demopage.htm")

# print(x)
# print(x.text)
# print(x.status_code)
# print(x.headers)
# print(x.json)

class w3schools_API:

    def w3_text():
        response_w3_text=requests.get("https://w3schools.com/python/demopage.htm")
        return response_w3_text.text
    
    def w3_status_code():
        response_w3_staus_code=requests.get("https://w3schools.com/python/demopage.htm")
        return response_w3_staus_code.status_code
    
    def w3_error_code():
        response=requests.get("https://w3schools.com/python/demopage.html")
        return response.status_code
    
    def w3_headers():
        response_w3_headers=requests.get("https://w3schools.com/python/demopage.htm")
        return dict(response_w3_headers.headers)



class dummy_API:

    def dummy_text():
        response_text=requests.get("https://dummy.restapiexample.com/api/v1/employees")
        return response_text.text


    def dummy_status_code():
        response_status_code=requests.get("https://dummy.restapiexample.com/api/v1/employees")
        # print(response_status_code)
        return response_status_code.status_code


    def dummy_headers():
        response_headers=requests.get("https://dummy.restapiexample.com/api/v1/employees")
        return dict(response_headers.headers)





