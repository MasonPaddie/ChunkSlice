from flask import Flask
from .extensions import mongo
from .main.routes import main


def create_app(config_object='ChunkSlice.settings'):
    app = Flask(__name__)

    app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

    app.config.from_object(config_object)

    mongo.init_app(app)

    app.register_blueprint(main)

    return app
  
