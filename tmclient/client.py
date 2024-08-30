import requests

class TMClient:
    def __init__(self, api_key, namespace):
        self.api_key = api_key
        self.namespace = namespace
        self.base_url = "https://api.testmail.app/api/json"

    def get_data(self):
        params = {
            'apikey': self.api_key,
            'namespace': self.namespace,
            'pretty': 'true'
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()
