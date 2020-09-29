from selenium import webdriver
from selenium.webdriver.common.by import By
class ZhuCe:
    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/?from=0014100135')

    def zhuce(self,corpname,managername,phonenumber,vcode):
        self.driver.find_element(By.ID,'corp_name').send_keys(corpname)
        self.driver.find_element(By.CSS_SELECTOR,'.js_corp_industry_btn').click()
        self.driver.find_element(By.CSS_SELECTOR,'[data-name="IT服务"]').click()
        self.driver.find_element(By.CSS_SELECTOR,'data-name="计算机软件/硬件/信息服务"').click()
        self.driver.find_element(By.CSS_SELECTOR,'#corp_scale_btn').click()
        self.driver.find_element(By.CSS_SELECTOR,'').click()
        self.driver.find_element(By.CSS_SELECTOR, '#corp_scale_btn ul li:nth-child(1)').click()s
        # corp_scale_btn > div > ul > li.qui_dropdownMenu_item.ww_dropdownMenu_item.ww_dropdownMenu_item_Curr
        self.driver.find_element(By.ID,'manager_name').send_keys(managername)
        self.driver.find_element(By.ID,'register_tel').send_keys(phonenumber)
        self.driver.find_element(By.CSS_SELECTOR,'#get_vcode').click()
        self.driver.find_element(By.ID,'vcode').send_keys(vcode)

        self.driver.find_element(By.ID,'iagree').click()
        self.driver.find_element(By.ID,'submit_btn').click()
        return self
