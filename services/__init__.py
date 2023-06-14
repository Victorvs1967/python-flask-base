from flask import Request
from werkzeug.security import check_password_hash

from app import db
from models import Book, User


######## User Servises ############

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

######## Books Servises ############

# Create Book
def create_book(request: Request):
  book = Book(
    request.json['title'],
    request.json['author'],
    request.json['year']
  )
  db.book.insert_one(book.__dict__)
  return book

# Update Book details
def edit_book(id: str, request: Request):
  book = User(
    request.json['title'],
    request.json['author'],
    request.json['year'],
  )
  book.set_id(id)
  db.book.replace_one({ '_id': id }, book.__dict__)
  return book

# Delete Book from database
def delete_book(id: str):
  result = db.dook.delete_one({ '_id': id })
  return result

# Get Book details from database using user_id
def get_book(id: str) -> Book:
  book = db.book.find_one({ '_id': id })
  return book

# Get Book list from database
def books_list():
  books = db.book.find({})
  return list(books)

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
