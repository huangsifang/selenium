from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.modityOrderPage import modityOrder
from page_obj.buyPage import buy

class modityOrderTest(myunit.MyTest):
	''' 洽谈订单测试 '''

	def test_modity_order(self):
		po = modityOrder(self.driver)
		po.modity_order()

		# 验证订单状态
		self.assertEqual(po.check_order_state(), "待供应商确认订单")
		function.insert_img(self.driver, "user_pawd_true.jpg")

if __name__ == "__main__":
	unittest.main()