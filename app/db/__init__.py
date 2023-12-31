from flask import g
from pymongo import MongoClient


config = {
  'host': 'localhost', # host for develop
  # 'host': 'database', # host for docker image
  'port': 27017,
  'username': '',
  'password': ''
}

class Client:
  def __new__(cls, database):
    client = MongoClient(**config)
    return client[database]

def get_db():
  if 'db' not in g:
    g.db = Client('users_db')
  return g.db
