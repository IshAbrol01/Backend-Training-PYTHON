import threading as th
from threading import *
import time
t1 = time.time()
time.sleep(1)
t2 = time.time()
print(t2-t1)

# def cube(num):
#     print("Cube is:- {}".format(num * num * num))

# def square(num):
#     print("Square is:- {}".format(num * num))

def login_signup(name):
    print("Hello {}, Welcome to CubexO".format(str(name)))
    print("Please Login / Sign Up before Proceeding Ahead")

def cookies():
    cookie_result=str(input("Accept or Reject Cookies:- "))
    time.sleep(20)
    return cookie_result

def main_body():
    print("This is the main body of of a Webpage or an Application the user wants to Access")

def cookie_status(cookie_result):
    print("Before Block")
    if(cookie_result.lower=='yes'):
        print("Cookies Accepted")
    else: print("Cookies NOT accepted")
    print("After Block")

if __name__ == "__main__":
    # thread1=th.Thread(target=square,args=(10,))
    # thread2=th.Thread(target=cube,args=(10,))
    thread3=th.Thread(target=login_signup,args=("Ish",))
    thread4=th.Thread(target=main_body)
    thread5=th.Thread(target=cookies,args=1,daemon=True)
    thread6=th.Thread(target=cookie_status)

    # thread1.start()
    # thread2.start()
    
    thread6.start()

    thread5.start()

    thread3.start()

    thread4.start()
    
    