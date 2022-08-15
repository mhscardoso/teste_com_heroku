from flask import Flask
from app.config import ConfigDev, ConfigProd
from app.extensions import db, migrate, ma, jwt

from app.users.routes import user_api
from app.messages.routes import message_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(ConfigDev)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(user_api)
    app.register_blueprint(message_api)

    return app