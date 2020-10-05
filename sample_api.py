import flask
import json
from flask_cors import CORS, cross_origin
from flask import Flask,request,jsonify,Response


app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/hello": {"origins": "http://localhost:port"}})

@app.route('/hello',methods= ['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
 
def hello():
    return "Hello, World!"

if __name__ == '__main__':
 app.run(debug=True)