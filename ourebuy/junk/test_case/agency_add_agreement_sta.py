from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.agencyAddAgreementPage import agencyAddAgreement
from page_obj.entryPage import entry

class agencyAddAgreementTest(myunit.MyTest):
	''' 新增协议测试 '''

	def test_agency_add_agreement(self):
		entry(self.driver).entry("agency")
		po = agencyAddAgreement(self.driver)
		po.agency_add_agreement()

		# 验证协议状态
		# self.assertEqual(po.check_agreement_state(), "待发送卖家")
		function.insert_img(self.driver, "user_pawd_true.jpg")

if __name__ == "__main__":
	unittest.main()