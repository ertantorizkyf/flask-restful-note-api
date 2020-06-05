# package import
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# file import
from config import app_config

# init sqlalchemy
db = SQLAlchemy()

# init marshmallow
ma = Marshmallow()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    # init db
    db.init_app(app)
    
    # init migration
    migrate = Migrate(app, db)
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    # init api
    api = Api(app)

    # init CORS
    CORS(app)

    # init routes
    from app.routes import routes
    routes(app, api)

    return app
