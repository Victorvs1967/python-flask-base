from pymongo import MongoClient


config = {
  'host': 'localhost', # host for develop
  # 'host': 'database', # host for docker image
  'port': 27017,
  'username': '',
  'password': ''
}

class Connection:
  def __new__(cls, database):
    connection = MongoClient(**config)
    return connection[database]