from flask import render_template, Blueprint, abort
from blog_data import blog_posts

blog = Blueprint("blog", __name__)

@blog.route("/blog")
def blogz():
    return render_template("blog.html", posts=blog_posts)

@blog.route("/blog/<slug>")
def blog_post(slug):
    post = next((p for p in blog_posts if p['slug'] == slug), None)

    if post:
        return render_template('blog_post.html', post=post)
    else:
        abort(404)

