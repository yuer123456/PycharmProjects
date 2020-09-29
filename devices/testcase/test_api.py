import json
import random

import requests
from requests import post

from devices.deviceapi.api import Api
from devices.deviceapi.login import Login


class TestApi:

    s = requests.session()

    @classmethod
    def setup_class(cls):

        cls.api=Api()
        cls.api.login()#degnlu

    def test_login(self):
        assert self.api.login()['status'] == 0
    def test_list(self):
        assert self.api.list()['status'] == 0
    '''
        r = self.s.post("http://l-cuedocker1.dev.cn2.corp.agrant.cn:32097/api/instore/list",
                        json={
                            "queryString": "", "repoId": "beijing",
                            "pageSize": 10, "pageNumber": 1},
                        )
        print(r.json())
        assert r.json()['status'] == 0
     '''
    def test_xinzeng(self):
        assert self.api.xinzeng()['status'] == 0
    def test_devicemodel(self):
        assert self.api.devicemodel()['status'] == 0
    def test_deviceinfolist(self):
        assert self.api.deviceinfolist()['status'] == 0

    def test_outstorelist(self):
        assert self.api.outstorelist()['status'] == 0

        '''
        这个犯了很多错误。1。想要节省代码，把s=requests.session() 放到类变量里，然后setup登录也用了，可是下面s
        还是有红色错误标识。最后琢磨半天，问了好多人，才发现是s是类变量，下面方法用的时候，需要self.s

        3.一个接口需要随机数，我写了个随机数，结果总是获取不到macid。我把macid = random.randint(1, 100000)
        放到类变量里了，然后定义的方法 也加上参数了，所以执行的时候报错。最后才知道，类变量不需要传参
         def test_xinzeng(self，macid):
        r = self.s.post("http://l-cuedocker1.dev.cn2.corp.agrant.cn:32097/api/instore/createV2",
                   params={'deviceTypeId': 'camera', 'subDeviceTypeId': 'camera_ip'},
                   json={"inStoreType": 0, "deviceTypeId": "camera", "subDeviceTypeId": "camera_ip",
                         "modelId": "CB20-S02", "purchaseRequestNo": "214124", "purchaseNo": "1234124", "cashNo": "",
                         "companyId": "nanjinganyuji", "repoId": "beijing", "deliveryMethod": 1, "trackingNo": "",
                         "consignee": "", "referredPerson": "122112", "referredPersonContact": "121212", "comment": "",
                         "address": "",
                         "deviceList": [
                             {"macId": self.macid, "deviceCode": "1243124124", "subModelId": "4mm", "checkStatus": 1}]})
        print(self.macid)
        print(r.json())
        assert r.json()['status'] == 0

        不会灵活运用犯的错误

        '''



