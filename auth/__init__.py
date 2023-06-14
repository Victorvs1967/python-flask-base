from flask import request
from flask_cors import CORS
from flask_restful import Resource
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import check_password_hash

from app import app, api, db
from services import create_user


# secret string generated with code: node -e "console.log(require('crypto').randomBytes(256).toString('base64'));"
app.config['JWT_SECRET_KEY'] = 'FxONLsEWZwMWVaSE5fngTdlvlRIHseTNSQz4xD1wR9gPn0cq9LBIm8os3NI7wlhKLcNjm9OwGYRRehXDMLqIqVBXZ1u+IbVaBh545dV8a/+4ZtifVMhicuexAJOJ4ST1GrfTCMnTlwNPcIDsTqCblryeyLSrpUyi3EZnwxEIjC87AIdUoRY+XAfOLABWjP+/uEQ8EcfzcRti3wHkusaa5yiYkXvvrPRsdcrzAFxRm3bHfutVbRDtvBHoKYTGHWw6VKmHitMPB+S6wz1LTa2GPDq/xObP6RH9nvoUEcY9oNa/TWrzo8gU9wQs0zOwNgGcfr6nsgWXfRtqVkFD6KnRjg=='
jwt = JWTManager(app)
CORS(app)

class Login(Resource):
  def post(self):
    username = request.json['username']
    password = request.json['password']
    user = self.authenticate(username, password)
    if user:
      token = create_access_token(identity={
        'username': username,
        'role': 'admin',
      }, expires_delta=False)
      return { 'token': token }
    return { 'error': 'Invalid username or password' }

  def authenticate(self, username, password):
    user = db.user.find_one({ 'username': username })
    if user and check_password_hash(user.get('password'), password):
      return user
    return None

class Signup(Resource):
  def post(self):
    if self.is_exist('username') or self.is_exist('email'):
      return { 'error': 'Username or email already exist.' }
    user = create_user(request=request)
    return user.__dict__

  def is_exist(self, key: str):
    username = request.json[key]
    user = db.user.find_one({ key: username })
    if user:
      return True
    return False

api.add_resource(Login, '/auth/login')
api.add_resource(Signup, '/auth/signup')
