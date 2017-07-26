from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.entryMarketPage import entryMarket

class entryMarketTest(myunit.MyTest):
	''' 进入超市测试 '''

	def test_entry_market(self):
		entryMarket(self.driver).entry_market()
		function.insert_img(self.driver, "user_pawd_true.jpg")

if __name__ == "__main__":
	unittest.main()