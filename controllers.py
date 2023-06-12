import json, re
from flask.globals import current_app
from markupsafe import escape
# Import flask dependencies
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

# Import task functions
from app.tasks import web_message

from uuid import uuid4
import requests
import urllib.parse

# Importing send email from sender
from .sender import send_mail, html_import, send_sms

# Import module models
from app.models.Flow import Flow
from app.models.Conversation import Conversation
from app.models.Tag import Tag
from config import allowed_domains, main_server_domain

# Define the blueprint: 'twilio', set its url prefix: app.url/twilio
twilio_mod = Blueprint('twilio', __name__, url_prefix='/api/v1')

# Twilio email endpoint
api_key         = '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' # SendGrid API Key of a user
from_email      = 'surekachetan09@gmail.com' # Email ID from which the mail is to be sent
to_emails       = ['surekachetanfr09@gmail.com'] # List of emails to send to
subject         = 'Testing bots on flask server' # Subject of the Email 
bot_link        = 'https://smart.mind-view.com/'
html_file       = 'app\\integrations\\twilio\\Template.html' # Grabs the html file
html_content    = html_import(html_file, bot_link)

@twilio_mod.route('/twilio/send/mail', methods=["POST"])
@cross_origin(allowed_domains)
def send():
    response = send_mail(from_email, to_emails, subject, html_content, api_key)
    if response == 202:
        print("Mails sent successfully!")
        return 'ok'
    return 'error'


# SMS endpoint
account_sid = 'AC2c748672589fabb9bd832f1ff14d7b97'
auth_token = 'e48f5ceabc9758240dac7d16d7441ac8'
sender = '+16085858947'
recipients = ['+918822585182', '+917976374375']
body = '\nSending test message pt-2.\nCan you please click this link: https://smart.mind-view.com/\n\nReport me back if it works!!'

@twilio_mod.route('/twilio/send/sms', methods=["POST"])
@cross_origin(allowed_domains)
def sendSMS():
    response = send_sms(account_sid, auth_token, sender, recipients, body)
    if response:
        print("Sent the sms!", response)
        return 'ok'
    return 'error'
