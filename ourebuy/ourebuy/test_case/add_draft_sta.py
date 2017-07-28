from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.addDraftPage import addDraft

class addDraftTest(myunit.MyTest):
	''' 新增汇票 '''

	def test_add_draft(self):
		po = addDraft(self.driver)
		po.add_draft()

		# 验证订单状态
		# self.assertEqual(po.check_order_state(), "待供应商确认订单")
		function.insert_img(self.driver, "user_pawd_true.jpg")

if __name__ == "__main__":
	unittest.main()