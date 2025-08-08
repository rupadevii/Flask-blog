from flask import render_template, request, flash, Blueprint, session, redirect, url_for
from app.models import User
from app import db, bcrypt
# from app.main import main

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/contact", methods = ['GET', 'POST'])
def contact():
    errors = []
    if request.method == 'POST':
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # if not name:
        #     errors.append("Name is required.")
        # if not email or '@' not in email:
        #     errors.append("Valid email is required.")
        # if not message:
        #     errors.append("Message cannot be empty.")

        if not name or '@' not in email or not message:
            flash("Please fill out all fields.", "error")
        else:
            flash("Message sent successfully!", "success")

        # if not errors:
        #     return render_template("contact.html", success=True)
    
    return render_template("contact.html")

@main.route("/team")
def team():
    members = [
        {"name" : "Rupa", "role" : "Frontend Developer"},
        {"name" : "Radha", "role" : "Backend Developer"},
        {"name" : "Anu", "role" : "UI/UX Designer"},
        {"name" : "Roshni", "role" : "Full-stack developer"},
        {"name" : "Priya", "role" : "Python developer"},
       ]
    return render_template("team.html", members = members)

@main.route("/register", methods= ["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        new_user = User(username=username, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash("Registered successfully ✅", "success")
        return redirect("/login")
    return render_template('register.html')

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password_input = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password_input):
            session["user_id"] = user.id
            session["username"] = user.username
            # flash(f"Welcome back, {user.username}!", "success")
            return redirect(url_for("main.home"))
        else:
            flash("Invalid username or password", "error")
            return redirect(url_for("main.login"))

    return render_template("login.html")

@main.route("/logout")
def logout():
    # session.clear()
    session.pop('user_id', None)
    # flash("You have been logged out.", "info")
    return redirect(url_for('main.home'))

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404