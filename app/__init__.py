from flask import Flask
from app.models import User
from flask_bcrypt import Bcrypt
import os
from app.extensions import db, login_manager

bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'site.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'

    from app.main.routes import main
    from app.blog.routes import blog

    app.register_blueprint(main)
    app.register_blueprint(blog, url_prefix = "/blog")

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
