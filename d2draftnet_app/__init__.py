from flask import Flask
from .config import HEROS

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    return app
