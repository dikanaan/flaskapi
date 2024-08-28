from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json, os

app = Flask(__name__)

api = Api(app)
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


basedir = os.path.dirname(os.path.abspath(__file__))
 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "db.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True




class Voucer(db.Voucer):
    id = db.Coloumn(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.Integer)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return True
        

db.create_all()


#XXXX
class appi(Resource):
    def get(self):
        
        
       
        return {"msg":"halo"}
    
    def post(self):
        dtusername = request.form["username"]
        dtpassword = request.form["password"]


        voucer = Voucer(username=dtusername, password=dtpassword)
        voucer.save

        response = {"msg":"berhasil input","code":200}
        return response, 200
    
api.add_resource(appi, "/voucer", methods=["GET", "POST"])




if __name__ == '__main__':
    app.run(debug=True, port=5000)