from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.page import login
from test_selenium2.pages import zhuce


class WeiDengLu:
    def set_up(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/?from=0014100135')
    def goto_login(self):
        self.driver.find_element(By.LINK_TEXT,'企业登录')
        return login
    def goto_zhuce(self):
        pass
    def lijizhuce(self):
        self.driver.find_element(By.LINK_TEXT,'立即注册')
        return zhuce
    def xiazai(self):
        self.driver.find_element(By.CSS_SELECTOR,'.index_top_operation_registerBtn').click()
        return self

