from app.apis.resources import *
from app.extensions import api

api.add_namespace(category_ns)
api.add_namespace(author_ns)
api.add_namespace(book_ns)
