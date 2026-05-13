from flask import current_app as app
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Post, Tag, Comment
from .forms import LoginForm, PostForm, CommentForm
from . import db


@app.route("/")
def index():
    q = request.args.get("q", "")
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).order_by(Post.created_at.desc()).all()
    else:
        posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template("index.html", posts=posts, q=q)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    return render_template("post.html", post=post, form=form)


@app.route("/post/<int:post_id>/comment", methods=["POST"])
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        c = Comment(author=form.author.data, body=form.body.data, post=post)
        db.session.add(c)
        db.session.commit()
        flash("Comment added", "success")
    return redirect(url_for("post_detail", post_id=post.id))


@app.route("/admin/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in", "success")
            return redirect(url_for("index"))
        flash("Invalid credentials", "danger")
    return render_template("login.html", form=form)


@app.route("/admin/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out", "info")
    return redirect(url_for("index"))


@app.route("/admin/post/new", methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data)
        tag_names = [t.strip() for t in form.tags.data.split(",") if t.strip()]
        for name in tag_names:
            tag = Tag.query.filter_by(name=name).first()
            if not tag:
                tag = Tag(name=name)
            post.tags.append(tag)
        db.session.add(post)
        db.session.commit()
        flash("Post created", "success")
        return redirect(url_for("post_detail", post_id=post.id))
    return render_template("edit_post.html", form=form)


@app.route("/admin/post/<int:post_id>/edit", methods=["GET", "POST"])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm(obj=post)
    if request.method == "GET":
        form.tags.data = ", ".join([t.name for t in post.tags])
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        post.tags.clear()
        tag_names = [t.strip() for t in form.tags.data.split(",") if t.strip()]
        for name in tag_names:
            tag = Tag.query.filter_by(name=name).first()
            if not tag:
                tag = Tag(name=name)
            post.tags.append(tag)
        db.session.commit()
        flash("Post updated", "success")
        return redirect(url_for("post_detail", post_id=post.id))
    return render_template("edit_post.html", form=form, post=post)


@app.route("/admin/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted", "info")
    return redirect(url_for("index"))
