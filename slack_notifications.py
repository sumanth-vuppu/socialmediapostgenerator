import os

import requests

from  dotenv import load_dotenv
load_dotenv()

SLACK_WEBHOOK_URL=os.getenv("SLACK_WEBHOOK_URL")


def notify_slack(message):
    payload = {"text": f":warning: {message}"}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    if response.status_code != 200:
        print(f"Failed to send notification: {response.text}")



