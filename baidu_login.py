# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BaiduLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_baidu_login(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        # driver.add_cookie({'name':'BAIDUID','value':'88CAF196E71BB5433049F3946FF9EF4A:FG=1'})
        driver.add_cookie({'name':'BDUSS','value':'lHenQ4a1BsdmU4MFF0WWpzUnl5cFRFdGE0TXFuWHVwUWQ1Y3QtSnlURWwycUJaTUFBQUFBJCQAAAAAAAAAAAEAAABLzdh3cGFsdWx1YQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACVNeVklTXlZVV'})
        '''
        driver.find_element_by_css_selector("#u1 > a[name=\"tj_login\"]").click()
        driver.find_element_by_id("TANGRAM__PSP_10__userName").clear()
        driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("17816869682")
        driver.find_element_by_id("TANGRAM__PSP_10__password").clear()
        driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("a65332794")
        driver.find_element_by_id("TANGRAM__PSP_10__verifyCode").clear()
        driver.find_element_by_id("TANGRAM__PSP_10__verifyCode").send_keys(u"稍大")
        driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
        '''
        driver.refresh()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        pass
        # self.driver.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
