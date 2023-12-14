from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

api = Api(version = '1.0', title = 'API Document ',description='This API for Book Inventory and Management System')
db = SQLAlchemy()