from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.entryPage import entry

class entryTest(myunit.MyTest):
	''' 进入超市测试 '''

	def test_entry(self):
		entry(self.driver).entry("agency")
		function.insert_img(self.driver, "user_pawd_true.jpg")

if __name__ == "__main__":
	unittest.main()