from cloudinary_image_service import get_cloudinary_image_url
from gemini_ai import generate_description_and_image
from instagram_api import instagram_post_api
from  prompts import prompts
import time
if __name__=="__main__":
    for prompt in prompts.values():
        instagram_post_result = generate_description_and_image(prompt)
        image_url= get_cloudinary_image_url()
        time.sleep(5)
        instagram_post_api(instagram_post_result,image_url)

