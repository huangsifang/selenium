import csv
from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import login

class loginTest(myunit.MyTest):
	''' 登录测试 '''

	# 测试用户登录
	def user_login_verify(self, username="", password="", code=""):
		login(self.driver).user_login(username, password, code)

	def test_login(self):
		# 用户名、密码错误
		data = csv.reader(open('ourebuy/data/login.csv', 'r'))
		for user in data:
			self.user_login_verify(username=user[0], password=user[1], code="0")
			po = login(self.driver)
			try:
				self.assertEqual(po.error_hint(), user[2])
			except AssertionError as msg:
				print(msg)
			function.insert_img(self.driver, "user_pawd_true.jpg")

	def test_login2(self):
		# login(self.driver).user_login_cookies()
		# 用户名、密码正确
		self.user_login_verify(username="zsbuy508", password="zsbuy508", code="0")
		sleep(2)
		po = login(self.driver)
		self.assertEqual(po.user_login_success(), "007846")
		function.insert_img(self.driver, "user_pawd_true.jpg")

if __name__ == "__main__":
	unittest.main()