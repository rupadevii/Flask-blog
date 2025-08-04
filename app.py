from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

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