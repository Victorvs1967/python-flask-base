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

def edit_user(id: str, request: Request):
  user_db = db.user.find_one({ '_id': id })
  user = User(
    request.json['username'],
    user_db.get('password'),
    request.json['email'],
    request.json['first_name'],
    request.json['last_name']
  )
  user.set_id(id)
  db.user.replace_one({ '_id': id }, user.__dict__)
  return user

def delete_user(id: str):
  result = db.user.delete_one({ '_id': id })
  return result

def get_user(id: str) -> User:
  user = db.user.find_one({ '_id': id })
  return user

def users_list():
  users = db.user.find({})
  return list(users)