from flask import render_template,request,redirect,url_for
from ..main import BlogForm, CommentForm
from . import main
from ..models import User, Comment, Blog, Subscriber
from datetime import datetime
from request import get_quotes
from .. import db

@main.route('/')
def index():
    '''
    view function to display index page and its content
    '''
    
    title='Post-Blog'
    return render_template('index.html', head=title,)


@main.route("/blog/new", methods=["POST", "GET"])
def new_blog():
    newblogform = BlogForm()
    if newblogform.validate_on_submit():
        blog_title = newblogform.blog_title.data
        newblogform.blog_title.data = ""
        blog_content = newblogform.blog_content.data
        newblogform.blog_content.data = ""
        new_blog = Blog(blog_title=blog_title,blog_content=blog_content,posted_at=datetime.now(),)
        new_blog.save_blog()

        
        subscriber = Subscriber.query.all()  
        return redirect(url_for(".index", id=new_blog.id))
    return render_template("new_blog.html",newblogform=newblogform)



@main.route("/blog/<int:id>", methods=["POST", "GET"])
def write_comment(id):
    blog = Blog.getBlogId(id)
    comment = Comment.get_comments(id)
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        comment_form.comment.data = ""
        new_comment = Comment(comment=comment,blog_id=blog.id)
        new_comment.save_comment()
        return redirect(url_for(".write_comment", id=blog.id))
    return render_template("comment.html",comment_form=comment_form,comment=comment,blog=blog)

# Function to delete blog
@main.route("/blog/<int:id>/delete")

def delete_comment(id):
    comment = Comment.getCommentId(id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for(".write_comment", id=comment.id))

# Function to update blog
@main.route('/subscribe')
def subscribe():

    subs = Subscriber(email=current_user.email)
    db.session.add(subs)
    db.session.commit()
    subs.save_subscriber()
    return redirect(url_for("main.index"))


@main.route("/blog/<int:id>/delete")
def delete_blog(id):
    blog = Blog.getBlogId(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for(".index", id=blog.id))





#Function to update blog
@main.route('/update/<int:id>', methods=['GET', 'POST'])
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

