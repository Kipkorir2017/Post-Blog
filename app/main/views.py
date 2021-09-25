from flask import render_template, request, redirect,url_for,flash,abort
from ..main.forms import BlogForm, CommentForm
from flask import render_template, request
from . import main
from .. import db
from ..requests import get_quote
from ..models import User, Comment, Blog, Subscriber
from flask_login import current_user
from datetime import datetime
from flask_login import login_required
from app.email import mail_message, sub_message


@main.route("/", methods=["GET", "BLOG"])
def index():
    blogs = Blog.get_all_blogs()
    quote = get_quote()
    title="Post-Blog"
    return render_template("index.html",blogs=blogs,quote=quote,head=title)


@main.route("/blog/<int:id>", methods=["POST", "GET"])
@login_required
def write_comment(id):
    blog = Blog.getBlogId(id)
    comment = Comment.get_comments(id)
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        comment_form.comment.data = ""
        new_comment = Comment(comment=comment,
                              user_id=current_user.id,
                              blog_id=blog.id)
        new_comment.save_comment()
        return redirect(url_for(".write_comment", id=blog.id))

    return render_template("comment.html",comment_form=comment_form,comment=comment,blog=blog)




@main.route("/blog/<int:id>/delete",methods=['POST'])
@login_required
def delete_comment(id):
    comment = Comment.query.getCommentId(id)
    db.session.delete(comment)
    db.session.commit()
    flash('Your comment has been deleted!','success')
    return redirect(url_for(".write_comment", id=comment.id))




@main.route('/subscribe')
@login_required
def subscribe():

    subs = Subscriber(email=current_user.email)
    db.session.add(subs)
    db.session.commit()
    subs.save_subscriber()
    return redirect(url_for("main.index"))


@main.route("/blog/<int:id>/delete",methods=['POST'])
@login_required
def delete_blog(id):
    blog = Blog.query.getBlogId(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for(".index", id=blog.id))


@main.route("/blog/new", methods=["POST", "GET"])
def new_blog():
    newblogform = BlogForm()
    if newblogform.validate_on_submit():
        blog_title = newblogform.blog_title.data
        newblogform.blog_title.data = ""
        blog_content = newblogform.blog_content.data
        newblogform.blog_content.data = ""
        new_blog = Blog(blog_title=blog_title,blog_content=blog_content,posted_at=datetime.now(),user_id=current_user.id)
        new_blog.save_blog()

        # call email addresses from the subscriber table in db
        subscriber = Subscriber.query.all()
        for subs in subscriber:
            sub_message(blog_title,"email/subscription", subs.email, new_blog=new_blog)
        return redirect(url_for(".index", id=new_blog.id))
    return render_template("n_blog.html",
                           newblogform=newblogform)



@main.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update_blog(id):
    blog = Blog.query.get_or_404(id)
    form = BlogForm()
    if form.validate_on_submit():
        blog.blog_title = form.blog_title.data
        blog.blog_content = form.blog_content.data
        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('.index'))
    elif request.method == 'GET':
        form.blog_title.data = blog.blog_title
        form.blog_content.data = blog.blog_content
    return render_template('update.html', blog=blog, form=form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)