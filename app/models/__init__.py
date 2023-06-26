# from uuid import uuid1
from werkzeug.security import generate_password_hash

class User:
  def __init__(self, username: str, password: str, email: str, first_name: str, last_name: str):
    # self._id = str(uuid1().hex)
    self.username = username
    self.password = generate_password_hash(password)
    self.email = email
    self.first_name = first_name
    self.last_name = last_name

  def set_id(self, id):
    self._id = id

class Book:
  def __init__(self, title: str, author: str, year: str):
    # self._id = str(uuid1().hex)
    self.title = title
    self.author = author
    self.year = year

  def set_id(self, id):
    self._id = id
