from app import app, mail
from flask_mail import Message


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message('Reset password', sender=app.config['ADMINS'][0], [recipients])
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)