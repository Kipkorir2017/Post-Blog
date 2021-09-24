from flask import render_template, redirect,url_for
from app.main.forms import BlogForm, CommentForm
from . import main
from flask import render_template
from ..models import User, Comment,Blog
from request import get_quote


@main.route("/")
def index():
    '''
    view function to return index page

    '''
    blogs = Blog.get_all_blogs()
    quote = get_quote()

    title="Post-Blog"
    return render_template("index.html",blogs=blogs,quote=quote,head=title)



@main.route("/blog/<int:id>")

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