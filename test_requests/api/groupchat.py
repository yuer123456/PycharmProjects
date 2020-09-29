import json

import requests

class GroupChat:
    def list(self,offset,limit,token,**kwargs):
        #dang json 里面有更多数据的时候，参数要一个**kwargs
        json = { "offset": offset,"limit": limit}
        json.update(kwargs)
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list'
        r = requests.post(url,
                          params={"access_token": token},
                          json=json
                          )
        print(kwargs)
        print(json)
        print(json.update(kwargs))

        print(r.json())
        return r.json()
    def get(self,chat_id,token):
        return {}

    def get_detail(self,chat_id,token):
        '''
        url = 'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list'
        r = requests.post(url,
                          params={"access_token": token},
                          json={
                              "offset": 0,
                              "limit": 100
                          })
        print(r.json())
'''
        chat_id = r.json()['group_chat_list'][0]['chat_id']
        detail_url = 'https: // qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get'
        params = {"access_token": token}
        r = requests.post(detail_url, params,
                          json={
                              "chat_id": chat_id
                          }
                          )
        print(json.dumps(r.json(), indent=2))
        return r.json()

