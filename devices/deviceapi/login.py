import json
import random

import requests
from requests import post


class Login:

    s = requests.session()


    def login(self):
        login_url = 'http://l-cuedocker1.dev.cn2.corp.agrant.cn:32097/api/auth/login'

        r = self.s.post(login_url, json={"password": "12345678", "username": "junfeng.li"})
        return self





