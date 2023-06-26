from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import request

from app.services import delete_user, edit_user, get_user, users_list


class Users(Resource):
  @jwt_required()
  def get(self):
    return users_list()

class User(Resource):
  @jwt_required()
  def delete(self, id):
    if delete_user(id):
      return { 'message': f'User with id: { id } deleted' }
    return { 'error': 'User not found.' }

  @jwt_required()
  def put(self, id):
    user = edit_user(id, request)
    if user:
      user['_id'] = str(user['_id'])
      return user.__dict__
    return { 'error': 'User not found.' }

  @jwt_required()
  def get(self, id):
    user = get_user(id)
    if user:
      user['_id'] = str(user['_id'])
      return user.__dict__
    return { 'error': 'User not found.' }
