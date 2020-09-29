import requests
class TestQJu:
    s=requests.session()
    authorization='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXJyZW50VGltZU1pbGxpcyI6IjE2MDEyMTQ4Mzk3MzgiLCJtb2JpbGUiOiIxNTgxMjM0NTY3OCIsInVzZXJOYW1lIjoiY2VzaGlseSIsImV4cCI6MTYwMTI1MDgzOSwidXNlcklkIjoiZjg4MTY0ZTZmMmYzNDI3ZDk0ZDhmMmJhMzEwNjgxNGEiLCJ1c2VyQ29kZSI6Ik5WQzAwMDAwMDA0In0.zUZR4-Gqoo5nXqkXSotK03qcpPDpMuBd3tjJ2vAosmU'
    def setup(self):
        url = 'http://l-test12.dev.cn2.corp.agrant.cn:9010/api/auth/login'
        mobile = 15812345678
        password = "e10adc3949ba59abbe56e057f20f883e"
        self.s.post(url,
                        json={"mobile": mobile, "password": password},
                        headers={'Content-Type': 'application/json'})



    def test_login(self):
        url='http://l-test12.dev.cn2.corp.agrant.cn:9010/api/auth/login'
        mobile=15812345678
        password="e10adc3949ba59abbe56e057f20f883e"
        r=self.s.post(url,
                      json={"mobile":mobile,"password":password},
                      headers={'Content-Type':'application/json'})
        print(r.json())
        assert r.json()['code'] == 20000
    def test_permssion(self):
        url = 'http://l-test12.dev.cn2.corp.agrant.cn:9010/api/user/permission'
        r = self.s.get(url,

                        headers={'Content-Type': 'application/json',
                                 'Authorization': self.authorization}
                                 )
        print(r.json())
        assert r.json()['code'] == 20000


    def test_loout(self):
        pass



