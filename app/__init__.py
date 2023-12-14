from flask import Flask
from app.extensions import db, api
from app.config import Config
from app.apis import api


def create_app():

    app = Flask(__name__)

    # config
    config = Config()
    app.config.from_object(config)

    # init extensions
    db.init_app(app)
    api.init_app(app)

    return app
