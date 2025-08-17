from flask import render_template, Blueprint, abort, request, flash, redirect, url_for
from blog_data import blog_posts
from flask_login import login_required, current_user
from app import db
from app.models import Post, User
from app.main.forms import PostForm
from datetime import datetime, timezone

blog = Blueprint("blog", __name__)

@blog.route("/blog")
def blogz():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template("blog.html", posts=posts)

@blog.route("/blog/<int:post_id>")
def blog_post(post_id):
    # post = next((p for p in blog_posts if p['slug'] == slug), None)
    post = Post.query.get_or_404(post_id)

    if post:
        return render_template('blog_post.html', post=post)
    else:
        abort(404)

@blog.route("/edit/<int:post_id>", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author != current_user.username:
        abort(403)

    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        flash("Post updated successfully!", 'success')
        return redirect(url_for('blog.blog_post', post_id=post.id))
    
    return render_template('blog/edit_post.html', post=post)

@blog.route('/add_post', methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title = form.title.data,
            content = form.content.data,
            author = current_user.username,
            date_posted = datetime.now(timezone.utc)
        )
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('blog.blogz'))
    return render_template('create_post.html', form=form, legend='New Post')

@blog.route('/delete/<int:post_id>', methods=["GET", "POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user.username:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('blog.blogz'))

@blog.route('/dashboard')
@login_required
def dashboard():
    posts = Post.query.filter_by(author=current_user.username).order_by(Post.date_posted.desc()).all()
    print("Posts found:", posts) 
    return render_template('dashboard.html', posts=posts, user=current_user)