import requests
import json


class API:
    API_URL = "https://api.vk.com/method/"

    def __init__(self, access_token, version):
        self.access_token = access_token
        self.version = version

    def get_friends(self, user_id, parameters):
        full_parameters = {'user_id': user_id,
                           'access_token': self.access_token,
                           'v': self.version}
        full_parameters.update(parameters)
        result = requests.get(f'{API.API_URL}friends.get', full_parameters)
        return json.loads(result.text)
