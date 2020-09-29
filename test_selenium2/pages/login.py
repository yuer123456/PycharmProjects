from selenium import  webdriver
from selenium.webdriver.common.by import By

from test_selenium2.pages import zhuce


class Login:
    def set_up(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_0014100135&ref_from=myhome_ref_sem_baidu_p')
    def saomaogin(self):
        pass
    def goto_zhuce(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT,'企业注册')
        return zhuce

