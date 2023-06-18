from flask import Flask
from flask_restful import Api

from db import Client


app = Flask(__name__)
db = Client('users_db')
api = Api(app)


from auth import *
from routes import *
from users import *