from flask import Flask , render_template , jsonify , request
import json

data=[{"id":1,"first_name":"Ish","last_name":"Abrol"},
      {"id":2,"first_name":"Bhoomi","last_name":"Samadhiya"},
      {"id":3,"first_name":"Krati","last_name":"Sengar"}]

app=Flask(__name__)

@app.route("/get_data",methods=['GET'])
def demo_api_get():
    return jsonify(data)

@app.route("/post_data",methods=['POST'])
def demo_api_post():
    data.append()

if __name__=="__main__":
    app.run(debug=True)