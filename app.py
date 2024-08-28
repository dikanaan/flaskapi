from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json, os

app = Flask(__name__)

api = Api(app)
CORS(app)

data = {}


#XXXX
class appi(Resource):
    def get(self):

        response = data
        return response
    
    def post(self):
        username = request.form["username"]
        password = request.form["password"]
        data["username"] = username
        data["password"] = password
        response = {"msg" : "Data dimasukan"}
        return response
    
    


api.add_resource(appi, "/voucer", methods=["GET", "POST"])




if __name__ == '__main__':
    app.run(debug=True, port=5000)
