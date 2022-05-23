import os

import requests


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

        data = {
            "messaging_product": "whatsapp",
            "to": phone_number,
            "type": "template",
            "template": {"name": template_name, "language": {"code": language_code}},
        }
        
        response = requests.post(f"{self.API_URL}/messages", headers=self.headers, json=data)
        
        assert response.status_code == 200, "Error sending message"
        
        return response.json()
    
    def process_webhook_notification(self, data):
        """_summary_: Process webhook notification
            For the moment, this will return the type of notification
        """
        
        response =  []
        
        for entry in data['entry']:
            
            for change in entry['changes']:
                response.append({
                    "type": change['field'],
                    "from": change['display_phone_number'],
                    "messages": change['messages'],
                    "errors": change['errors'],
                    "contacts": change['contacts'],
                })
                
        return response
