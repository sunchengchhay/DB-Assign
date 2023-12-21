from flask_restx import fields
from app.extensions import api

output_category_model = api.model(
    'Category Output Model', {
        'id': fields.Integer,
        'name': fields.String
    }
)

output_author_model = api.model(
    'Author Output Model', {
        'id': fields.Integer,
        'name': fields.String,
        'gender': fields.String,
        'date_of_birth': fields.String,
        'nationality': fields.String
    }
)


output_book_model = api.model(
    'Author Output Model', {
        'id': fields.Integer,
        'category': fields.Nested(output_category_model),
        'author': fields.Nested(output_author_model),
        'language': fields.String,
        'title': fields.String,
        'publication_date': fields.String,
        'available': fields.Boolean
    }
)
