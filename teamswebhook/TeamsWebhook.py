import requests
import json
from datetime import datetime

class TeamsWebhook:

    def __init__(self, url:str = "", script_name:str = "Webhook", 
                 image_url:str = "https://learnersgalaxy.ai/wp-content/uploads/2024/01/Python-Symbol.png"):
        self.url = url
        self.script_name = script_name
        self.image_url = image_url

    def request_post(self, message:str):
        data = {
                "type": "message",
                "attachments": [
                    {
                        "contentType": "application/vnd.microsoft.card.adaptive",
                        "contentUrl": None,
                        "content": {
                            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                            "type": "AdaptiveCard",
                            "version": "1.2",
                            "body": [
                                {
                                    "type": "TextBlock",
                                    "size": "medium",
                                    "weight": "bolder",
                                    "text": self.script_name,
                                    "style": "heading",
                                    "wrap": True
                                },
                                {
                                    "type": "TextBlock",
                                    "spacing": "none",
                                    "text": f"Event occured at: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}",
                                    "isSubtle": True,
                                    "wrap": True
                                },
                                {
                                    "type": "Image",
                                    "url": self.image_url,
                                    "altText": "Python",
                                    "size": "medium"
                                },
                                {
                                    "type": "TextBlock",
                                    "text": message
                                }
                            ]
                        }
                    }
                ]
            }    
        r = requests.post(self.url, data = json.dumps(data), headers={"Content-Type":"application/json"})