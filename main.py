from json import loads
from time import sleep
from typing import Any, Dict
from common.utils import send_rsvp_email

# --- MAIN HANDLER ---
def lambda_handler(event: Dict[str, Any], context: Any = None):
    """
    AWS Lambda entry point for consuming RSVP notification messages and sending emails.
    """
    for record in event.get('Records', []):
        try:
            body = loads(record['body'])
            send_rsvp_email(
                full_name=body['full_name'],
                mail=body['mail'],
                side=body['side'],
                guest=body['guest'],
                status=body['status']
            )
            sleep(0.1)
        except Exception as e:
            raise f"Error processing SQS message: {e}"
