from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
	'''
	用户登录页面
	'''

	url = '/'

	# Action
	bbs_login_user_loc = (By.XPATH, "//*[@id='mzCust']/div/div[1]/img")
	bbs_login_button_loc = (By.ID, "mzLogin")

	def bbs_login(self):
		self.find_element(*self.bbs_login_user_loc).click()
		sleep(1)
		self.find_element(*self.bbs_login_button_loc).click()

	login_username_loc = (By.ID, "account")
	login_password_loc = (By.ID, "password")
	login_button_loc = (By.ID, "login")

	# 登录用户名
	def login_username(self, username):
		self.find_element(*self.login_username_loc).send_keys(username)

	# 登录密码
	def login_password(self, passeord):
		self.find_element(*self.login_password_loc).send_keys(passeord)

	# 登录按钮
	def login_button(self):
		self.find_element(*self.login_button_loc).click()

	# 定义统一登录入口
	def user_login(self, username="username", passeord="1111"):
		""" 获取的用户名密码登录 """
		self.open()
		self.bbs_login()
		self.login_username(username)
		self.login_password(passeord)
		self.login_button()
		sleep(1)

	error_hint_loc = (By.XPATH, "//*[@id='mainForm']/div[2]/span[1]")
	user_login_success_loc = (By.ID, "mzCustName")

	# 错误提示
	def error_hint(self):
		return self.find_element(*self.error_hint_loc).text

	# 登录成功用户名
	def user_login_success(self):
		return self.find_element(*self.user_login_success_loc).text

