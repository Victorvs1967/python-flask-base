from flask import Request

from app import db
from models import User


def create_user(request: Request):
  user = User(
    request.json['username'],
    request.json['password'],
    request.json['email'],
    request.json['first_name'],
    request.json['last_name'],
  )
  db.user.insert_one(user.__dict__)
  return user

def users_list():
  users = db.user.find({})
  return list(users)