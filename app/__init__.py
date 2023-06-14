from flask import Flask
from flask_restful import Api

from db import Connection

app = Flask(__name__)
api = Api(app)
db = Connection('users_db')

from auth import *
from users import *
from routes import *