from flask import request
from flask_cors import CORS
from flask_restful import Resource
from flask_jwt_extended import JWTManager, create_access_token

from app import app
from app.services import create_user, authenticate, is_exist


# secret string generated with code: node -e "console.log(require('crypto').randomBytes(256).toString('base64'));"
app.config['JWT_SECRET_KEY'] = 'FxONLsEWZwMWVaSE5fngTdlvlRIHseTNSQz4xD1wR9gPn0cq9LBIm8os3NI7wlhKLcNjm9OwGYRRehXDMLqIqVBXZ1u+IbVaBh545dV8a/+4ZtifVMhicuexAJOJ4ST1GrfTCMnTlwNPcIDsTqCblryeyLSrpUyi3EZnwxEIjC87AIdUoRY+XAfOLABWjP+/uEQ8EcfzcRti3wHkusaa5yiYkXvvrPRsdcrzAFxRm3bHfutVbRDtvBHoKYTGHWw6VKmHitMPB+S6wz1LTa2GPDq/xObP6RH9nvoUEcY9oNa/TWrzo8gU9wQs0zOwNgGcfr6nsgWXfRtqVkFD6KnRjg=='
app.config['JWT_ACCESS_TOKEN_EPIRES'] = 86400000

jwt = JWTManager(app)
CORS(app)

class Login(Resource):
  def post(self):
    username = request.json['username']
    password = request.json['password']
    user = authenticate(username, password)
    if user:
      token = create_access_token(identity={
        'username': username,
        'role': 'ADMIN',
      })
      return { 'token': token }
    return { 'error': 'Invalid username or password' }

class Signup(Resource):
  def post(self):
    if is_exist('username', request.json['username']) or is_exist('email', request.json['email']):
      return { 'error': 'Username or email already exist.' }
    user = create_user(request=request)
    user['_id'] = str(user['_id'])
    return user
