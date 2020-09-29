import json
import token

import requests


class TestWeWork:
    tokenurl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    corpid = 'wwc907d68d285797ae'
    secret = 'wQIR_nBBKIfWnhuZNGnLE-P8_cz0NZkFKRvSpzyBrCg'
    #secret = 'u5Esm7-7yYInD9P7IeAgAoG9Xu_Z9JNIejr2o4qIbxs'
    token=None
    #因为token其他接口也需要，所以把这个获取token的接口放到setup 的一个类方法中，加上装饰器S
    @classmethod
    def setup_class(cls):
        params = {"corpid": cls.corpid,
                  "corpsecret": cls.secret
                  }

        r = requests.get(cls.tokenurl, params)
        print(r.json())
        assert r.json()["errcode"] == 0
        cls.token = r.json()["access_token"]

    #def test_asscess_token(self):
     #   params = {"corpid": self.corpid,
      #        "corpsecret":self.secret
       #       }

        #r=requests.get(self.tokenurl,params)
        #print(r.json())
        #assert r.json()["errcode"]==0
        #self.token=r.json()["access_token"]
    def test_get_token_exist(self):
        assert self.token is not None

    def test_get_groupchat_list(self):

        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list'
        r=requests.post(url,
                       params={"access_token":self.token},
                       json={
                           "offset": 0,
                           "limit": 100
                       })
        print(r.json())
        assert r.json()["errcode"]==0

        
    def test_groupchat_detail(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list'
        r = requests.post(url,
                         params={"access_token": self.token},
                         json={
                             "offset": 0,
                             "limit": 100
                         })
        print(r.json())
       
        chat_id = r.json()['group_chat_list'][0]['chat_id']
        detail_url='https: // qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get'
        params={"access_token":self.token}
        r=requests.post(detail_url,params,
                        json={
                            "chat_id": chat_id
                        }
                        )
        print(json.dumps(r.json(),indent=2))
        assert r.json()['errcode']==0
        assert len(r,json()['group_chat'['member_list']])>0





