from app import app
from flask import render_template



@app.route('/')
def index():
    '''
    view function to return index page

    '''
    title="Post-Blog"
    return render_template('index.html', head=title)