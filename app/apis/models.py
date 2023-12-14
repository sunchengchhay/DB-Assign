from flask_restx import fields
from app.extensions import api

output_category_model = api.model(
    'Category Output Model',{
        'id':fields.Integer,
        'name':fields.String
    }
)