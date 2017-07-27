# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Ourebuy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.ourebuy.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ourebuy(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        driver.add_cookie({'name':'Market.ourebuy.com','value':'zsbuy508*7cdc161f137047b3b931508aa3b87b50','domain':'.ourebuy.com'})
        # driver.add_cookie({'name':'Market.ourebuy.com','value':'zsbuy508*b3980a73c05c4f59bfbd449b7495ff40','domain':'.ourebuy.com'})
        '''
        self.driver.switch_to.frame(driver.find_element_by_id("con_dl_iframe"))
        driver.find_element_by_id("uid").clear()
        driver.find_element_by_id("uid").send_keys("zsbuy508")
        driver.find_element_by_id("kl").clear()
        driver.find_element_by_id("kl").send_keys("zsbuy508")
        driver.find_element_by_id("randCode").clear()
        driver.find_element_by_id("randCode").send_keys("0")
        driver.find_element_by_id("loginBt").click()
        driver.find_element_by_link_text(u"我的平台").click()
        driver.find_element_by_xpath("//img[contains(@src,'http://files.ourebuy.com/images/cngc/newPage/pingtai_img1.jpg')]").click()
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
