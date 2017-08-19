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

		'''
		# 买方采购订单-待处理订单
		po.entry_order()

		# 验证订单状态
		self.assertEqual(po.check_order_state(), "待承兑汇票支付")

		# 点击登记承兑汇票
		po.login_draft()
		'''

		# 买方承兑汇票管理-承兑汇票管理
		po.entry_draft()

		po.add_draft()

		# 验证票状态
		self.assertEqual(po.check_draft_state(), "待提交")

		# 提交汇票
		po.submit_draft()
		
		function.insert_img(self.driver, "user_pawd_true.jpg")

if __name__ == "__main__":
	unittest.main()