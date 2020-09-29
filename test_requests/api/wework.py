from datetime import datetime

import requests
class WeWork:
    tokenurl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    #youyu不同的seret对应不通的token,suoyi,token dingyiweiyigezidian
    token=dict()
    corp_id= 'wwc907d68d285797ae'
    secret = 'wQIR_nBBKIfWnhuZNGnLE-P8_cz0NZkFKRvSpzyBrCg'

#以下改造于get_tokenfangfa
    @classmethod
    def get_token(cls, secret):
        if secret is None:
            return cls.token[secret]
        #避免重复请求
        if secret not in cls.token.keys():
            r = cls.get_access_token(secret)

            cls.token = r.json()["access_token"]
            cls.token_time[secret]=datetime.now()
        return cls.token[secret]
    @classmethod
    def get_access_token(cls,secret):
        r = requests.get(cls.tokenurl, params={
            "corpid": cls.corpid,
            "corpsecret": secret
        }
                         )
        return cls
        print(r.json())




        '''
    @classmethod
    def get_token(cls,secret):

        r = requests.get(cls.tokenurl, params = {
            "corpid": cls.corpid,
            "corpsecret": secret
                  }
                         )
        print(r.json())

        cls.token = r.json()["access_token"]
        '''

