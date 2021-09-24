from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import Required


class BlogForm(FlaskForm):
    '''
    Form to allow you  add blog

    '''
    blog_title = StringField('Title:', validators=[Required()])
    blog_content = TextAreaField('Blog:', validators=[Required()])
    submit = SubmitField('Submit:')


class CommentForm(FlaskForm):
    '''
    Form for creating a blog comment

    '''
    comment = TextAreaField('Comment on Blog')
    submit = SubmitField('Submit')


class UpdateBlogForm(FlaskForm):
    blog_title = StringField("Title", validators=[Required()])
    blog_content = TextAreaField("Comment", validators=[Required()])
    submit = SubmitField("Update")




class UpdateProfile(FlaskForm):
    username = StringField("Username")
    bio = TextAreaField("Bio")
    email = StringField("Email")
    submit = SubmitField("Update")





