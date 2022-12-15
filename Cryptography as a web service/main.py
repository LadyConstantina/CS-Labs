from PlayService import Play
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate
from argon2 import PasswordHasher
import requests
import random
import uuid
import win32com.client as win32
import pythoncom
import pyotp

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager = Manager(app)
password_hasher = PasswordHasher()

hotp = pyotp.HOTP('laboratorywork5')

class User(db.Model):

    #Table creation
    ID = db.Column(db.String(64), primary_key = True)
    Name = db.Column(db.String(32), unique = False)
    Surname = db.Column(db.String(32), unique = False)
    Email = db.Column(db.String(32), unique = True)
    Password = db.Column(db.String(32), unique = False)
    Access = db.Column(db.String(32), unique = False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/adduser",methods = ["POST"])
def Add_User():
    email = request.json["Email"]
    user_check = User.query.filter_by(Email = email).first()
    if user_check:
        return {
            "message": "There is already an user with this email!",
            "Code": 409
        },409
    else:
        index = str(uuid.uuid1())
        new_user = User(
                ID = index, 
                Name = request.json["Name"],
                Surname = request.json["Surname"],
                Email = request.json["Email"],
                Password = password_hasher.hash(request.json["Password"]),
                Access = request.json["Access"]
            )
        db.session.add(new_user)
        db.session.commit()
        return {
            "Index":index,
            "Status":"User created",
            "Code": 200
        },200

@app.route("/getaccess",methods = ["GET"])
def LogIn():
    email = request.json["Email"]
    password = request.json["Password"]
    user = User.query.filter_by(Email = email).first()
    if user:
        user_dict = user.__dict__
        if password_hasher.verify(user_dict["Password"],password):
            index_authentication = random.randrange(0,2000)
            code = hotp.at(index_authentication)
            send_email(email,code)
            code_in = input("We sent you an email with a code. Check and type it here: ")
            if hotp.verify(code_in, index_authentication):
                print("Welcome dear",user_dict["Name"],"!")
                Play(user_dict["Access"])
                return {
                    "Message":"You loged in successfully",
                    "Code":200
                },200
        else:
            return {
                "Message":"Incorrect Code! Try again!",
                "Code": 401
            }, 401
    else:
        return {
                "Message":"User could not be found!",
                "Code": 404
            }, 404


def send_email(to,code):
        outlook = win32.Dispatch('outlook.application', pythoncom.CoInitialize())
        mail = outlook.CreateItem(0)
        mail.To = to
        mail.Subject = "Authentication code!"
        mail.Body = "Your authentication code is: "+str(code)
        mail.Send()

app.run(host = "0.0.0.0",port = "5000")
