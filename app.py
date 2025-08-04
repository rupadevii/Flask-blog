from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    errors = []
    if request.method == 'POST':
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name:
            errors.append("Name is required.")
        if not email or '@' not in email:
            errors.append("Valid email is required.")
        if not message:
            errors.append("Message cannot be empty.")

        if not errors:
            return render_template("contact.html", success=True)
        
    return render_template("contact.html", errors=errors)
    
@app.route("/team")
def team():
    members = [
        {"name" : "Rupa", "role" : "Frontend Developer"},
        {"name" : "Radha", "role" : "Backend Developer"},
        {"name" : "Anu", "role" : "UI/UX Designer"},
        {"name" : "Roshni", "role" : "Full-stack developer"},
        {"name" : "Priya", "role" : "Python developer"},
       ]
    return render_template("team.html", members = members)

if __name__ == "__main__":
    app.run(debug=True)