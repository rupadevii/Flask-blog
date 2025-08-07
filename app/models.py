from app import db
from datetime import datetime, timezone

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # date_posted = db.Column(db.DateTime, default=datetime)
    date_posted = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    author = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<Post {self.title}>'
