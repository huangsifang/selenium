from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from .loginPage import login

class entryMarket(Page):
	'''
	用户进入网上超市个人中心
	'''
	url = '/'

	# Action
	my_platform_loc = (By.LINK_TEXT, "我的平台")
	my_market_platform_loc = (By.XPATH, "/html/body/div[4]/div/div[3]/a/img")
	# my_market_platform_loc = (By.CSS_SELECTOR, "body > div.mainbody > div > div.fr.mrgT30.platform_right > a > img")

	def entry_market(self):
		login(self.driver).user_login("zsbuy508", "zsbuy508", "0")
		self.find_element(*self.my_platform_loc).click()
		sleep(1)
		self.find_element(*self.my_market_platform_loc).click()