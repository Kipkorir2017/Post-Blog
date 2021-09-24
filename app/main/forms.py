from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import Required


class BlogForm(FlaskForm):
    """
    Form to allow you  add blog
    """
    blog_title = StringField('Title', validators=[Required()])
    blog_content = TextAreaField("Blog:", validators=[Required()])
    submit = SubmitField('Submit')





