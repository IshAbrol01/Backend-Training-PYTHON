import asyncio
import time
import threading
import requests
import json
# print("""USING ASYNCHRONOUS PROGRAMMING TO BUILD A TEMPLATE FOR A WEBSITE THAT HAS THREE COMPONENTS :- 
#       \n 1) COOKIES SETTING \n 2) LOGIN / SIGN UP \n 3) MAIN CONTENT OF WEBPAGE""")

# string1="""HELLO1""" #Size is :- 6
# string3='''HELLO 1'''#Size is :- 7
# string2="""HELLO
# 1""" #Size is :- 7
# string4="HELLO \n 1"  #Size is :- 9
# print(string4)
# print(type(string4))
# print(len(string4))



# # print(time.time())
# async def test0():
#     print("Statement 1")
#     await asyncio.sleep(1)
#     print("Statement 2")
#     await asyncio.sleep(1)

# def test():
#     print("Statement 1")
#     time.sleep(1)
#     print("Statement 2")
#     time.sleep(1)

# def test1():
#     print("Statement 1")
#     time.sleep(1)
#     print("Statement 2")
#     time.sleep(1)



# t1=time.time()
# asyncio.run(test0())
# t2=time.time()
# print(t2-t1)

# t3=time.time()
# test()
# t4=time.time()
# print(t4-t3)

# thread1=threading.Thread(target=test1)

# t5=time.time()
# thread1.start()
# thread1.join()
# t6=time.time()
# print(t6-t5)


# async def one_two():
#     print("One")
#     await asyncio.sleep(1)
#     print("Two")
#     await asyncio.sleep(1)
#     await three_four()
#     print("Five")
#     await asyncio.sleep(1)
#     print("Six")
#     await asyncio.sleep(1)

# async def three_four():
#     print("Three")
#     await asyncio.sleep(1)
#     print("Four")
#     await asyncio.sleep(1)

# asyncio.run(one_two())

# async def cookies():
#     global cookies_response
#     cookies_response = input("ACCEPT OR REJECT COOKIES")
    

# async def login_signup(name):
#     await cookies()
#     print("Hello {}, Please LOG IN / SIGN UP First to continue".format(name))
#     return 
    


# async def content(name):
#     await login_signup(name)
#     global numbers
#     numbers = [x for x in range(1,10000000001)]
#     for i in numbers:
#         print(i,end=" ")
#     print("Cookies Acceptance Status :- ",cookies_response)

# global name
# name="Ish"

# asyncio.run(content(name))



'''Script to convert JSON file to Python Readable Formats [LIST in this Case]'''
# result=requests.get('https://dummyapi.online/api/movies')
# print(type(result.json()))
# print(len(result.json()))
# print(result.json()[0])


class synchronous:

    def __init__(self):
        self.api_1_movies()
        self.api_2_blogs()
        self.api_3_user()


    def api_1_movies(self):
        # API 1 :- 10 Movies
        
        result1=requests.get('https://dummyapi.online/api/movies')
        print("\n",result1.json()[0],"\n")
        return result1


    def api_2_blogs(self):
        # API 2 :- 10 Blogs

        result2=requests.get('https://dummyapi.online/api/blogposts')
        print("\n",result2.json()[0],"\n")
        return result2


    def api_3_user(self):
        #API 3 :- 10 Users
        
        result3=requests.get('https://dummyapi.online/api/users')
        print("\n",result3.json()[0],"\n")
        return result3
    
    


class asynchronous:


    def __init__(self):
        
        asyncio.run(self.a_api_1_movies())
        print("_________")
        time.sleep(5)
        # await self.a_api_1_movies()
        asyncio.run(self.a_api_2_blogs())
        print("_________________")
        # await self.a_api_2_blogs()
        asyncio.run(self.a_api_3_user())
        # await self.a_api_3_user()
        


    async def a_api_1_movies(self):
        # API 1 :- 10 Movies
        
        a_result1=requests.get('https://dummyapi.online/api/movies')
        print("\n",a_result1.json()[0],"\n")
        return a_result1


    async def a_api_2_blogs(self):
        # API 2 :- 10 Blogs
        
        a_result2=requests.get('https://dummyapi.online/api/blogposts')
        print("\n",a_result2.json()[0],"\n")
        return a_result2

    async def a_api_3_user(self):
        #API 3 :- 10 Users
    
        a_result3=requests.get('https://dummyapi.online/api/users')
        print("\n",a_result3.json()[0],"\n")
        return a_result3
    



class asynchronous_with_threading:


    def __init__(self):
        if __name__=="__main__":
            thread1=threading.Thread(target=self.a_t_api_1_movies,daemon=True)
            thread2=threading.Thread(target=self.a_t_api_2_blogs,daemon=True)
            thread3=threading.Thread(target=self.a_t_api_3_user,daemon=True)
            thread1.start()
            thread2.start()
            thread3.start()
            thread1.join()
            thread2.join()
            thread3.join()


    def a_t_api_1_movies(self):
        # API 1 :- 10 Movies
        
        a_t_result1=requests.get('https://dummyapi.online/api/movies')
        print("\n",a_t_result1.json()[0],"\n")
        return a_t_result1


    def a_t_api_2_blogs(self):
        # API 2 :- 10 Blogs
        
        a_t_result2=requests.get('https://dummyapi.online/api/blogposts')
        print("\n",a_t_result2.json()[0],"\n")
        return a_t_result2

    def a_t_api_3_user(self):
        #API 3 :- 10 Users
    
        a_t_result3=requests.get('https://dummyapi.online/api/users')
        print("\n",a_t_result3.json()[0],"\n")
        return a_t_result3





sync_time_start=time.time()
obj1=synchronous()
sync_time_end=time.time()
sync_time_result=sync_time_end-sync_time_start
# print("Time Taken by SYNCRONOUS Function is :- ",sync_time_end-sync_time_start)


async_time_start=time.time()
obj2=asynchronous()
async_time_end=time.time()
async_time_result=async_time_end-async_time_start
# print("Time Taken by ASYNCHRONOUS Function is :- ",async_time_end-async_time_start)


async_thread_time_start=time.time()
obj3=asynchronous_with_threading()
async_thread_time_end=time.time()
async_thread_time_result=async_thread_time_end-async_thread_time_start
# print("Time Taken by ASYNCHRONOUS Function with THREADING is :- ",async_thread_time_end-async_thread_time_start)



print("\nResults :- ")
print("SYNCHRONOUS TIME",sync_time_result,"\n")
print("ASYNCHRONOUS TIME",async_time_result,"\n")
print("ASYNCHRONOUS WITH THREAD",async_thread_time_result,"\n")



# response = requests.get('https://dummyapi.online/api/movies')
# if response.status_code == 200:
#     data = json.loads(response.text)
# print(data)
# print(type(data))

