from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from services import books_list, create_book


class Books(Resource):
  @jwt_required()
  def post(self):
    book = create_book(request=request)
    return book.__dict__

  @jwt_required()
  def get(self):
    return books_list()

class Book(Resource):
  def get(self):
    pass

  def put(self):
    pass

  def delete(self):
    pass