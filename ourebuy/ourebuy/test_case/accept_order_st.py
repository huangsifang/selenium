from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.acceptOrderPage import acceptOrder

class acceptOrderTest(myunit.MyTest):
	''' 接受订单测试 '''

	def test_accept_order(self):
		po = acceptOrder(self.driver)
		po.entry_home_check_order()

		# 验证订单状态
		self.assertEqual(po.check_order_state(2, 7), "待接受")

		po.accept_order()

		po.check_suspense_order()

		# 验证订单状态
		self.assertEqual(po.check_order_state(1, 6), "待承兑汇票支付")

		function.insert_img(self.driver, "user_pawd_true.jpg")

if __name__ == "__main__":
	unittest.main()