from app import create_app, db
from app.models import User, Post

app = create_app()
app.app_context().push()

db.create_all()

print("Tables created successfully!")

# Sample user
user1 = User(username="rupa", email="rupa@example.com", password="securepass123")

# Sample post
post1 = Post(title="My First Blog Post", content="Hello world from Flask!", author="rupa")

# Add and commit to DB
db.session.add(user1)
db.session.add(post1)
db.session.commit()

print("🎉 Sample data inserted!")
