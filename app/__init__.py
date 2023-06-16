from flask import Flask
from .views import home


def create_app(config=None):

    app = Flask(__name__)

    if config:
        app.config.from_object(config)

    # blueprints
    app.register_blueprint(home)

    return app
