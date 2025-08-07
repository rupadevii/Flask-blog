from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'site.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.main.routes import main
    from app.blog.routes import blog

    app.register_blueprint(main)
    app.register_blueprint(blog, url_prefix = "/blog")

    return app

db = SQLAlchemy()