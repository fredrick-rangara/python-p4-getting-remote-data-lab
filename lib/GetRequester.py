import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Change .text to .content to return bytes
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # get_response_body now returns bytes, 
        # which json.loads can handle perfectly.
        body = self.get_response_body()
        return json.loads(body)