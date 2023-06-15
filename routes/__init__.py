from app import api
from auth import Login, Signup
from books import Book, Books
from users import User, Users


# Auth routes
api.add_resource(Login, '/auth/login')
api.add_resource(Signup, '/auth/signup')

# Users routes
api.add_resource(Users, '/api/users')
api.add_resource(User, '/api/users/<id>')

# Books routes
api.add_resource(Books, '/api/books')
api.add_resource(Book, '/api/books/<id>')