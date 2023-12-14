import os
from .db import DB

class Config():
    DEBUG = True
    APP_NAME = "Book Inventory and Management System"
    SECRET_KEY = b'soy,bsrolanhoun@@@IL0veY0u==<3xD:3-\*'
    SQLALCHEMY_DATABASE_URI = DB().sqlite_uri()