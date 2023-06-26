from bson import ObjectId
from flask import Request
from werkzeug.security import check_password_hash

from models import Book, User
from db import get_db

######## User Servises ############

# Create User
def create_user(request: Request) -> User:
  db = get_db()
  user = User(
    request.json['username'],
    request.json['password'],
    request.json['email'],
    request.json['first_name'],
    request.json['last_name'],
  )
  db.user.insert_one(user.__dict__)
  return user.__dict__

# Update User details (w/o password)
def edit_user(id: str, request: Request) -> User:
  db = get_db()
  user_db = db.user.find_one({ '_id': ObjectId(id) })
  user = User(
    request.json['username'],
    user_db.get('password'),
    request.json['email'],
    request.json['first_name'],
    request.json['last_name']
  )
  # user.set_id(id)
  db.user.update_one({ '_id': ObjectId(id) }, { '$set': user.__dict__ })
  return user

# Delete User from database
def delete_user(id: str):
  db = get_db()
  return db.user.delete_one({ '_id': ObjectId(id) })

# Get User details from database using user_id
def get_user(id: str) -> User:
  db = get_db()
  return db.user.find_one({ '_id': ObjectId(id) })

# Get Users list from database
def users_list():
  db = get_db()
  users = []
  for user in list(db.user.find({})):
    user['_id'] = str(user['_id'])
    users.append(user)
  return users

######## Books Servises ############

# Create Book
def create_book(request: Request):
  db = get_db()
  book = Book(
    request.json['title'],
    request.json['author'],
    request.json['year']
  )
  db.book.insert_one(book.__dict__)
  return book

# Update Book details
def edit_book(id: str, request: Request):
  db = get_db()
  book = Book(
    request.json['title'],
    request.json['author'],
    request.json['year'],
  )
  # book.set_id(id)
  db.book.update_one({ '_id': ObjectId(id) }, {'$set': book.__dict__})
  return book

# Delete Book from database
def delete_book(id: str):
  db = get_db()
  return db.book.delete_one({ '_id': ObjectId(id) })

# Get Book details from database using user_id
def get_book(id: str) -> Book:
  db = get_db()
  return db.book.find_one({ '_id': ObjectId(id) })

# Get Book list from database
def books_list():
  db = get_db()
  return list(db.book.find({}))

# Auth services
def authenticate(username, password):
  db = get_db()
  user = db.user.find_one({ 'username': username })
  if user and check_password_hash(user.get('password'), password):
    return user
  return None

def is_exist(key: str, value: str):
  db = get_db()
  user = db.user.find_one({ key: value })
  if user:
    return True
  return False
