# importing modules
from twilio.rest import Client              # Used for sending sms
from sendgrid import SendGridAPIClient      # Used for Mails API
from sendgrid.helpers.mail import Mail      # Used for sending mails


#####################################
# Start of sending emails
#####################################
def html_import(filename, bot_link):
    """
    Description: Extracts HTML Data from provided the HTML file.
    Arguments - filename / filepath
    Returns - HTML Data
    """
    with open(filename, "r") as f:
        html_str = f.read()
    return html_str.format(bot=bot_link)


def send_mail(from_email, to_emails, subject, html_content, api_key):
    """
    Description: Sends emails to the list of recipients.
    Arguments - from_email, to_emails, subject, html_content, api_key
    Returns - Response code
    """
    
    sg_client = SendGridAPIClient(api_key)
    message = Mail(
        from_email = from_email,        # Sender mail
        to_emails = to_emails,          # Recipients
        subject = subject,              # Message subject
        html_content = html_content,    # HTML Content
    )
    response = sg_client.send(message)  # Sends message
    return response.status_code


#####################################
# Start of sending sms
#####################################
def send_sms(account_sid, auth_token, from_phone, to_phone, body):
    client = Client(account_sid, auth_token)
    for to_num in to_phone:
        message = client.messages.create(
            from_=from_phone,
            to=to_num,
            body=body
        )
    if message.sid:
        return message
    return "An error occoured"
