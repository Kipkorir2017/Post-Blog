from flask_mail import Message
from flask import render_template
# from app import mail
from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
mail = Mail(app)

sender_email = 'kipkorir1@gmail.com'
subject_pref = 'password'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'kipkorir1@gmail.com'
app.config['MAIL_PASSWORD'] = 'Benja312!'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


def mail_message(subject, template, to, **kwargs):
    email = Message(subject_pref + " : " + subject,
                    sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    mail.send(email)


def sub_message(subject, template, to, **kwargs):
    email = Message(subject_pref + " : " + subject,
                    sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    mail.send(email)


if __name__ == '__main__':
    app.run()
