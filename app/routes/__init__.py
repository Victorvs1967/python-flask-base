from flask_restful import Api

from app import app
from app.auth import Login, Signup
from app.books import Book, Books
from app.users import User, Users


api = Api(app)

# Auth routes
api.add_resource(Login, '/auth/login')
api.add_resource(Signup, '/auth/signup')

# Users routes
api.add_resource(Users, '/api/users')
api.add_resource(User, '/api/users/<id>')

# Books routes
api.add_resource(Books, '/api/books')
api.add_resource(Book, '/api/books/<id>')