from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.modityOrderPage import modityOrder

class modityOrderTest(myunit.MyTest):
	''' 洽谈订单测试 '''

	def test_modity_order(self):
		modityOrder(self.driver).modityOrder()
		function.insert_img(self.driver, "user_pawd_true.jpg")

if __name__ == "__main__":
	unittest.main()