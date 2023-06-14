from flask import Request
from werkzeug.security import check_password_hash

from app import db
from models import User


# Create User
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

# Update User details (w/o password)
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

# Delete User from database
def delete_user(id: str):
  result = db.user.delete_one({ '_id': id })
  return result

# Get User details from database using user_id
def get_user(id: str) -> User:
  user = db.user.find_one({ '_id': id })
  return user

# Get Users list from database
def users_list():
  users = db.user.find({})
  return list(users)

# Auth services
def authenticate(username, password):
  user = db.user.find_one({ 'username': username })
  if user and check_password_hash(user.get('password'), password):
    return user
  return None

def is_exist(key: str, value: str):
  user = db.user.find_one({ key: value })
  if user:
    return True
  return False
