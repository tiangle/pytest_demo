import json

import requests

from config.config import CONFIG
from exceptions.exceptions import ApiRequestError


class SmaApi:
    def __init__(self):
        self.timeout = CONFIG.TIME_OUT
        self.session = requests.Session()

    def submit(self, url, body):
        try:
            response = self.session.post(url, json=body, timeout=self.timeout)
            response.raise_for_status()
            response_test = json.loads(response.text)
            response_result = int(response_test["result"])
            response_desc = response_test["desc"]
            return {"result": response_result, "desc": response_desc}
        except Exception as e:
            raise ApiRequestError from e

    def __del__(self):
        if hasattr(self, "session"):
            self.session.close()