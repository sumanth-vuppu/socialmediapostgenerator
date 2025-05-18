
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import calendar
from dotenv import load_dotenv
import os
import time

import slack_notifications


gmt = time.gmtime()

import platform
from pathlib import Path
from io import BytesIO
from PIL import Image
from datetime import datetime
load_dotenv()
gemini_key=os.getenv("GEMINI_KEY")

current_file_name=os.path.basename(__file__)
def generate_description_and_image(prompt):
    client = genai.Client(api_key=gemini_key)
    requirement=prompt
    #requirement=input("Enter your prompt: ")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-04-17",
            contents=[requirement+ "the description should able to read less than 5 mins. I need just output story it should not include searches context this content is for social media tailor for social media  the output should only the content and hashtags in telugu language "]
        )
    except Exception as e:
        slack_notifications.notify_slack(current_file_name +" : "+str(e))
    #print("Result: -----------"+response.text)
    caption= response.text
    try:

        image_prompt = client.models.generate_content(
            model="gemini-2.5-flash-preview-04-17",
            contents=[
                requirement + "the description should be as detailed as possible for image generation. I need just output story it should not include searches context this content is for social media tailor for social media  the output should contain the resolution 9:16. from all the content i need output just one best visual description do very deep research and provide answer"]
        )
    except Exception as  e:
        slack_notifications.notify_slack(current_file_name +" : "+str(e))


    #print("iamge result : -----------" + image_prompt.text)
    image_prompt = image_prompt.text



    client = genai.Client(api_key=gemini_key)
    try:

        contents = (image_prompt+"from that summary create a best and beautiful  image as detailed as you can for image generation i need the very best output hd quality for social media dont display text anywhere in image tailor  for social media  the output should contain the resolution a photo with a width of at least 1,080 pixels with an aspect ratio of between 1.91:1 and 4:5"
        )
    except Exception as  e:
        slack_notifications.notify_slack(current_file_name +" : "+str(e))

    response = client.models.generate_content(
        model="gemini-2.0-flash-preview-image-generation",
        contents=contents,
        config=types.GenerateContentConfig(
          response_modalities=['TEXT', 'IMAGE']
        )
    )

    for part in response.candidates[0].content.parts:
      if part.text is not None:
        pass
      elif part.inline_data is not None:
        image = Image.open(BytesIO((part.inline_data.data)))

        image.save("image.jpg")
        #image.show()
        return caption

