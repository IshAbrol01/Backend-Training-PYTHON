from flask import Flask , render_template , jsonify
import json
import pandas
import os
import requests
from datetime import datetime


# # data=[{"id":1,"first_name":"Ish","last_name":"Abrol"}]
# basefolder="Test KT"
# # df=pandas.DataFrame(data)
# # df.to_csv(os.getcwd()+f"/{basefolder}/test.csv") #/home/my/Desktop/Python/Backend-Training-Python
# column_ordering=[]
# global response

# response=requests.get("https://dummyjson.com/products/10")
#     # return response.json()
# response_data=response.json()
# df1=pandas.DataFrame(response_data)
# df1.to_csv(os.getcwd()+f"/{basefolder}/{datetime.now().date()}_aggregated.csv",index=False,colums=column_ordering)
# # print(os.getcwd())
# # print(datetime.now().date())

# # print(response_data)
# # print(type(response_data))

# # app=Flask(__name__)

# # @app.route("/test")
# # def login_page():
# #     return data.json()

# # if __name__ == "__main__":
# #     app.run(debug=True)
# # print(os.path)

list1=["a","b","c"]

df=pandas.DataFrame(list1)
df.to_csv(os.getcwd()+"test123.csv")


