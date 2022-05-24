import os
import requests

import json


class WhatsAppWrapper:

    API_URL = "https://graph.facebook.com/v13.0/"
    API_TOKEN = os.environ.get("WHATSAPP_API_TOKEN")
    NUMBER_ID = os.environ.get("WHATSAPP_NUMBER_ID")

    def __init__(self):
        self.headers = {
            "Authorization": "Bearer {}".format(self.API_TOKEN),
            "Content-Type": "application/json",
        }
        
        self.API_URL = "https://graph.facebook.com/v13.0/" + self.NUMBER_ID

    def send_template_message(self, template_name, language_code, phone_number):

        payload = {
            "messaging_product": "whatsapp",
            "to": phone_number,
            "type": "template",
            "template": {"name": template_name, "language": {"code": language_code}}
        }
        
        response = requests.request("POST", f"{self.API_URL}/messages", headers=self.headers, json=json.dumps(payload))
        
        print(response.request.body, response.request.url, response.json(), response.status_code)
        assert response.status_code == 200, "Error sending message"

        return response.status_code

    def process_webhook_notification(self, data):
        """_summary_: Process webhook notification
        For the moment, this will return the type of notification
        """

        response = []

        for entry in data["entry"]:

            for change in entry["changes"]:
                response.append(
                    {
                        "type": change["field"],
                        "from": change["display_phone_number"],
                        "messages": change["messages"],
                        "errors": change["errors"],
                        "contacts": change["contacts"],
                    }
                )

        return response
