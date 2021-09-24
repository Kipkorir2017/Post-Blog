
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model):
    '''
    User class to define user Objects

    '''
    __tablename__ = 'users'

    #create the columns for users table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_path = db.Column(db.String())
    blog = db.relationship("Blog", backref="user", lazy="dynamic")
    comment = db.relationship("Comment", backref="user", lazy="dynamic")


class  Blog(db.Model):
    '''
    Blog class to define Blog objects
    '''
    __tablename__ = 'blogs'
    #create the columns for blogs table
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String)
    blog_content = db.Column(db.String)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment = db.relationship('Comment', backref='blog', lazy="dynamic")

class Comment(db.Model):
    """
    comment model for each blog 
    """
    __tablename__ = 'comments'
    #Create  columns for the comments table
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    comment_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))


class Subscriber(db.Model):
    '''
    model class for subscribers
    '''
    __tablename__='subscribers'
    #Create columns for subscribers table
    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)
    


class Quote:
    """
    Quote class to define Quotes Objects
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote
