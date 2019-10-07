import logging

import azure.functions as func


def main(event: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event: %s',
                 event.get_body().decode('utf-8'))
    eventBody = event.get_body().decode('utf-8')
    if("test" in eventBody):
        print("custom event found")
