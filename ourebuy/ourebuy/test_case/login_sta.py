from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import login

class loginTest(myunit.MyTest):
	''' 社区登录测试 '''

	# 测试用户登录
	def user_login_verify(self, username="", password="", code=""):
		login(self.driver).user_login(username, password, code)
	'''
	def test_login(self):
		# 用户名、密码为空登录
		self.user_login_verify()
		po = login(self.driver)
		self.assertEqual(po.error_hint(), "请输入用户名!")
		function.insert_img(self.driver, "user_pawd_empty.jpg")
	'''
	def test_login2(self):
		# login(self.driver).user_login_cookies()
		# 用户名、密码正确
		self.user_login_verify(username="123", password="123", code="0")
		sleep(2)
		po = login(self.driver)
		self.assertEqual(po.user_login_success(), "007846")
		function.insert_img(self.driver, "user_pawd_true.jpg")

if __name__ == "__main__":
	unittest.main()