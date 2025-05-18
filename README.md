**Project Title**

Automated Instagram Content Generator & Uploader

---

## Overview

A Python script that leverages Google Gemini (gemini-2.5-flash-preview-04-17) for both text and image generation, Cloudinary for image storage, and the Instagram API for automated content posting. It also sends status notifications to Slack via incoming webhooks.

Key features:

* **Text Generation:** Uses Gemini for dynamic captions and post content.
* **Image Generation:** Uses Gemini to create relevant visuals for posts.
* **Image Hosting:** Uploads generated images to Cloudinary and retrieves the hosted URLs.
* **Instagram Upload:** Publishes the generated content to Instagram.
* **Slack Notifications:** Posts success or failure messages to a Slack channel.

---

## Prerequisites

* Python 3.8+
* Pip
* A Cloudinary account
* An Instagram account with a valid Instagram Graph API access token
* A Slack workspace with an incoming webhook URL
* Access to Google Gemini API

---

## Configuration

Create a `.env` file in the project root with the following environment variables:

```dotenv
# Gemini API Key
GEMINI_KEY=<YOUR_GEMINI_API_KEY>

# Instagram Credentials
INSTAGRAM_ACCESS_TOKEN=<YOUR_INSTAGRAM_ACCESS_TOKEN>
INSTAGRAM_ID=<YOUR_INSTAGRAM_BUSINESS_ACCOUNT_ID>

# Cloudinary Credentials
CLOUDINARY_CLOUD_NAME=<YOUR_CLOUD_NAME>
CLOUDINARY_API_KEY=<YOUR_CLOUDINARY_API_KEY>
CLOUDINARY_API_SECRET=<YOUR_CLOUDINARY_API_SECRET>
CLOUDINARY_PUBLIC_ID=<YOUR_CLOUDINARY_PUBLIC_ID>

# Slack Webhook URL
SLACK_WEBHOOK_URL=<YOUR_SLACK_INCOMING_WEBHOOK_URL>
```

> **Tips:**
>
> * To get your Gemini API key, visit [AI Studio Prompts - New Chat](https://aistudio.google.com/prompts/new_chat) and click **Get API Key**.
> * To generate your Instagram Access Token and ID, follow [OceanWP Guide](https://docs.oceanwp.org/article/487-how-to-get-instagram-access-token).
> * Retrieve Cloudinary credentials from your [Cloudinary Dashboard](https://cloudinary.com/documentation/developer_onboarding_faq_find_credentials).
> * Create a Slack Incoming Webhook via the [Slack API Webhooks page](https://api.slack.com/messaging/webhooks).

---

## Installation

1. **Clone the repository**

   ```bash
   git https://github.com/sumanth-vuppu/socialmediapostgenerator.git
   cd socialmediapostgenerator/
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Setup `.env`**
   Add all required keys to your `.env` as described above.

---

## Usage

Edit `prompts.py` to customize the content prompts. The prompts are stored in a dictionary—feel free to tweak them to suit your style.

Run the main script:

```bash
python main.py
```

> **Deployment Tip:**
> Deploy the script to a cloud server (e.g., AWS EC2, Google Cloud Compute) and schedule it via cronjobs or a similar task scheduler for automated recurring posts.

---

## Customization

* **Refine Responses:** Open `gemini_ai.py` and adjust the `contents` variable to fine-tune how the Gemini model generates text and images.
* **Add New Platforms:** Extend the script to support other social media platforms by following the existing modular structure.

---

## Troubleshooting

* **API Errors:** Ensure all environment variables are correctly set and valid.
* **Network Issues:** Confirm that your server or local machine has internet access and is not blocked by firewalls.
* **Cloudinary Upload Failures:** Check your Cloudinary usage quotas and permissions.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

---


