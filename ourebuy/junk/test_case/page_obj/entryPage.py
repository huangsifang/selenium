from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from .loginPage import login

class entry(Page):
	'''
	用户进入网上超市个人中心
	'''
	url = '/'

	login_frame_loc = (By.ID, "con_dl_iframe")
	my_platform_loc = (By.LINK_TEXT, "我的平台")
	junk_loc = (By.LINK_TEXT, "废旧物资")

	def entry(self, role):
		self.open()
		if role == "buyer":
			self.driver.add_cookie({'name':'Market.ourebuy.com','value':'zsbuy508*24ba303f2f434e5e94f8acfc44e5d0f9','domain':'.ourebuy.com'})
		elif role == "seller":
			self.driver.add_cookie({'name':'Market.ourebuy.com','value':'zssale508*98972ccb6a6a4e988963cada07feda70','domain':'.ourebuy.com'})
		else:
			self.driver.add_cookie({'name':'Market.ourebuy.com','value':'sfzhongjie808*366783f8f89040cdafff7f98111d9915','domain':'.ourebuy.com'})
		self.driver.refresh()
		self.driver.switch_to.frame(self.find_element(*self.login_frame_loc))
		self.find_element(*self.my_platform_loc).click()
		sleep(1)

		# 切换到我的平台窗口
		self.switch_to_current_window()
		self.find_element(*self.junk_loc).click()

