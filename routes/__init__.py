from app import api
from auth import Login, Signup
from users import User, Users


api.add_resource(Login, '/auth/login')
api.add_resource(Signup, '/auth/signup')
api.add_resource(Users, '/api/users')
api.add_resource(User, '/api/users/<id>')
