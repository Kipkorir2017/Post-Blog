from app import app
from flask import render_template
from .models import Blog
from request import get_quote


@app.route("/")
def index():
    '''
    view function to return index page

    '''
    blogs = Blog.get_all_blogs()
    quote = get_quote()

    title="Post-Blog"
    return render_template("index.html",blogs=blogs,quote=quote,head=title)