from dotenv import load_dotenv
import os

import slack_notifications
current_file_name=os.path.basename(__file__)

load_dotenv()
access_token = os.getenv("INSTAGRAM_ACCESS_TOKEN")
instagram_id=os.getenv("INSTAGRAM_ID")

import requests
def instagram_post_api(caption,image_url):
    # Endpoint
    url = "https://graph.facebook.com/v22.0/"+instagram_id+"/media"

    # Payload (JSON body)
    payload = {
        "image_url": image_url,
        "caption": caption
    }


    # Add access_token as a query param
    params = {
        "access_token": access_token
    }

    # Send POST request
    try:
        response = requests.post(url, params=params, data=payload)
    except Exception as  e:
        slack_notifications.notify_slack(current_file_name +" : "+str(e))

    # Print response
    print("Status Code:", response.status_code)
    if(response != 200):
        slack_notifications.notify_slack(current_file_name + " : " + str(response.json()))


    print("Response JSON:", response.json())
    container_result=response.json()
    try:
        container_id=container_result["id"]
    except Exception as  e:
        slack_notifications.notify_slack(current_file_name +"unable to get file id : "+str(e))




    # Facebook Graph API endpoint to publish media
    url = "https://graph.facebook.com/v22.0/"+instagram_id+"/media_publish"

    # Payload: pass the media `creation_id` you got from the previous step
    payload = {
        "creation_id": container_id
    }
    # Add access token as a query parameter
    params = {
        "access_token": access_token
    }

    # Send POST request
    try:
        response = requests.post(url, params=params, data=payload)
    except Exception as  e:
        slack_notifications.notify_slack(current_file_name +" : "+str(e))

    if (response != 200):
        slack_notifications.notify_slack(current_file_name + " : " + str(response.json()))

    # Print result
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
