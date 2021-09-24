from flask import render_template,request,redirect,url_for

from . import main

# from .request import get_quotes

@main.route('/')
def index():
    '''
    view function to display index page and its content
    '''
    
    title='Post-Blog'
    return render_template('index.html', head=title,)
