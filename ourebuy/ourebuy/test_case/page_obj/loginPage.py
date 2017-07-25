from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
	'''
	用户登录页面
	'''

	url = '/'

	login_frame_loc = (By.ID, "con_dl_iframe")
	login_username_loc = (By.ID, "uid")
	login_password_loc = (By.ID, "kl")
	login_code_loc = (By.ID, "randCode")
	login_button_loc = (By.ID, "loginBt")

	# 登录用户名
	def login_username(self, username):
		self.find_element(*self.login_username_loc).send_keys(username)

	# 登录密码
	def login_password(self, passeord):
		self.find_element(*self.login_password_loc).send_keys(passeord)

	# 登录验证码
	def login_code(self, code):
		self.find_element(*self.login_code_loc).send_keys(code)
	# 登录按钮
	def login_button(self):
		self.find_element(*self.login_button_loc).click()

	# 定义统一登录入口
	def user_login(self, username="username", passeord="1111", code="0"):
		""" 获取的用户名密码登录 """
		self.open()
		self.driver.switch_to.frame(self.find_element(*self.login_frame_loc))
		self.login_username(username)
		self.login_password(passeord)
		self.login_code(code)
		self.login_button()
		sleep(1)

	# 添加cookies登录
	def user_login_cookies(self):
		self.open()
		# self.driver.add_cookie({'name':'Market.ourebuy.com', 'value':'zsbuy508*0cd0ac964ba14b9b90dbf2c4a2fecb3c'})

	user_login_success_loc = (By.XPATH, "/html/body/div/div/ul/li[1]")

	# 错误提示
	def error_hint(self):
		alert = self.driver.switch_to_alert()
		info = self.driver.switch_to_alert().text
		self.driver.switch_to_alert().accept() # 必须关闭弹出框，否则截图会报错
		self.driver.switch_to.default_content() 
		return info

	# 登录成功用户名
	def user_login_success(self):
		return self.find_element(*self.user_login_success_loc).get_attribute("title")

