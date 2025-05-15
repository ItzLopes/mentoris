from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)

    from . import models

    from .routes import main
    app.register_blueprint(main)

    from .routes_app.alunos_routes import alunos_bp
    app.register_blueprint(alunos_bp)

    return app