from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import login

class loginTest(myunit.MyTest):
	''' 社区登录测试 '''

	# 测试用户登录
	def user_login_verify(self, username="", password=""):
		login(self.driver).user_login(username, password)

	def test_login(self):
		''' 用户名、密码为空登录 '''
		self.user_login_verify()
		po = login(self.driver)
		self.assertEqual(po.error_hint(), "请填写完整的登录信息")
		function.insert_img(self.driver, "user_pawd_empty.jpg")

	def test_login2(self):
		''' 用户名、密码正确 '''
		self.user_login_verify(username="17816869682", password="huangsifang123")
		sleep(2)
		po = login(self.driver)
		self.assertEqual(po.error_hint(), "请点击按钮进行验证")
		# self.assertEqual(po.user_login_success(), "17816869682")
		function.insert_img(self.driver, "user_pawd_true.jpg")

if __name__ == "__main__":
	unittest.main()