import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
import  os
from dotenv import load_dotenv

import slack_notifications
current_file_name=os.path.basename(__file__)

load_dotenv()
cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME")
api_key=os.getenv("CLOUDINARY_API_KEY")
api_secret=os.getenv("CLOUDINARY_API_SECRET")
public_id=os.getenv("CLOUDINARY_PUBLIC_ID")
def get_cloudinary_image_url():
    # Configuration
    cloudinary.config(
        cloud_name = cloud_name,
        api_key = api_key,
        api_secret =api_secret,
        secure=True
    )

    # Upload an image
    try:
        upload_result = cloudinary.uploader.upload(os.path.join(os.getcwd(), "image.jpg"),
                                               public_id=public_id)
    except Exception as  e:
        slack_notifications.notify_slack(current_file_name +" : "+str(e))
    print(upload_result["secure_url"])
    return upload_result["secure_url"]

