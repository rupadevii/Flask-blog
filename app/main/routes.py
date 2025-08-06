from flask import render_template, request, flash, Blueprint

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

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404