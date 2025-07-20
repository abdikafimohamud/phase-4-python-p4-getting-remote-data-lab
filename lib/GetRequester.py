# lib/GetRequester.py
import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Returns the raw response body as a string

    def load_json(self):
        response = requests.get(self.url)
        return response.json()  # Converts JSON response to a Python object (list/dict)
