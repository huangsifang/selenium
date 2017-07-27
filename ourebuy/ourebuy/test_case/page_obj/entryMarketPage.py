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
	login_frame_loc = (By.ID, "con_dl_iframe")
	my_platform_loc = (By.LINK_TEXT, "我的平台")
	my_market_platform_loc = (By.XPATH, "/html/body/div[4]/div/div[3]/a/img")

	def switch_to_current_window(self):
		all_handles = self.driver.window_handles

		current_windows = self.driver.current_window_handle
		for handle in all_handles:
			if handle != current_windows:
				self.driver.switch_to.window(handle)

	def entry_market(self):
		self.open()
		self.driver.add_cookie({'name':'Market.ourebuy.com','value':'zsbuy508*7cdc161f137047b3b931508aa3b87b50','domain':'.ourebuy.com'})
		self.driver.refresh()
		self.driver.switch_to.frame(self.find_element(*self.login_frame_loc))
		# login(self.driver).user_login("zsbuy508", "zsbuy508", "0")
		self.find_element(*self.my_platform_loc).click()
		sleep(1)

		# 切换到我的平台窗口
		self.switch_to_current_window()
		self.find_element(*self.my_market_platform_loc).click()

		# 切换到网上超市个人中心页面
		self.switch_to_current_window()

