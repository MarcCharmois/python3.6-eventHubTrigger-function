import logging
import os, json
import azure.functions as func
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def main(event: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event: %s',
                 event.get_body().decode('utf-8'))
    eventBody = event.get_body().decode('utf-8')
    apiKey =os.environ['SENDGRID_API_KEY']
    if("test" in eventBody):
        print("custom event found")
        messageText="custom event found"
        message = Mail(
            from_email='marc.charmois@charmoisdev.onmicrosoft.com',
            to_emails='marc.charmois@gmail.com',
            subject='Sending with Twilio SendGrid is Fun',
            html_content='<strong>and easy to do anywhere, even with Python</strong><br>custom event found'+ '<br>' + eventBody)
        try:
            sg = SendGridAPIClient(apiKey)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(str(e))