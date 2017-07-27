from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.buyPage import buy

class buyTest(myunit.MyTest):
	''' 购买商品测试 '''

	def test_buy(self):
		po = buy(self.driver)
		po.buy()

		# 验证订单状态
		self.assertEqual(po.check_order_state(po.current_order_id), "待供应商确认订单")
		function.insert_img(self.driver, "user_pawd_true.jpg")

if __name__ == "__main__":
	unittest.main()