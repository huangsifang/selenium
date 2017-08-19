from HTMLTestRunner import HTMLTestRunner
import smtplib
import unittest
import time
import os

if __name__ == '__main__':
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = './junk/report/' + now + 'result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(stream=fp,
		title='废旧物资竞价测试报告',
		description='环境: windows 7 浏览器: chrome')
	discover = unittest.defaultTestLoader.discover('./junk/test_case', pattern='*_sta.py')
	runner.run(discover)
	fp.close() # 关闭生成的报告