from typing import Any
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from services import books_list, create_book, delete_book, edit_book, get_book


class Books(Resource):
  @jwt_required()
  def post(self):
    book = create_book(request=request)
    return book.__dict__

  @jwt_required()
  def get(self):
    return books_list()

class Book(Resource):
  @jwt_required()
  def get(self, id):
    book = get_book(id)
    if book:
      return book
    return { 'error': 'Book not found.' }

  @jwt_required()
  def delete(self, id):
    if delete_book(id):
      return { 'message': f'Book with id: { id } deleted' }
    return { 'error': 'Book not found.' }

  @jwt_required()
  def put(self, id):
    book = edit_book(id, request)
    if book:
      return book.__dict__
    return { 'error': 'Book not found.' }
