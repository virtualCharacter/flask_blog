from flask import render_template, session, redirect, url_for, request
from .. import db
from ..models import User, Blog, Comment
from .forms import BlogForm
from ..decoration import login_required


from . import main

@main.route('/')
def index():
    blogs = Blog.query.all()
    return render_template('main/index.html', blogs=blogs)

@main.route('/publish', methods=['GET', 'POST'])
@login_required
def publish_blog():
    blogForm = BlogForm()
    if blogForm.validate_on_submit():
        title = blogForm.title.data
        abstract = blogForm.abstract.data
        article = blogForm.article.data
        user_id = session.get('user_id')
        blog = Blog(title=title, abstract=abstract, article=article)
        user = User.query.filter_by(id=user_id).first()
        blog.user = user
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('main/publish_blog.html', blogForm=blogForm)

@main.route('/detail/<blog_id>', methods=['GET', 'POST'])
def blog_detail(blog_id):
    comments = Comment.query.all()
    length = len(comments)
    blog_in_detail = Blog.query.filter_by(id=blog_id).first()
    return render_template('main/blog_detail.html', blog=blog_in_detail,
                           comments=comments, length=length)

@main.route('/add_comment/', methods=['POST'])
@login_required
def add_comment():
    comment_text = request.form.get('comment_text')
    blog_id = request.form.get('blog_id')
    user_id = session.get('user_id')

    user = User.query.filter_by(id=user_id).first()
    blog = Blog.query.filter_by(id=blog_id).first()
    comment = Comment(comment_text=comment_text, user=user, blog=blog)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('main.blog_detail', blog_id=blog_id))

#上下文处理器
@main.context_processor
def main_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter_by(id=user_id).first()
        if user:
            return {'user' : user}
    return {}

