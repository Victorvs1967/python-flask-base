from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app import api
from services import users_list


class Users(Resource):
  @jwt_required()
  def get(self):
    return users_list()


api.add_resource(Users, '/users')