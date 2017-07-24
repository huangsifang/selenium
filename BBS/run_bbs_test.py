from HTMLTestRunner import HTMLTestRunner
# from email.mime.text import MTMEText
# from email.header import Header
import smtplib
import unittest
import time
import os

if __name__ == '__main__':
	now = time.strftime("%Y-%m-%d %H_%M_%S")
	filename = './bbs/report/' + now + 'result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(stream=fp,
		title='魅族社区自动化测试报告',
		description='环境: windows 7 浏览器: chrome')
	discover = unittest.defaultTestLoader.discover('./bbs/test_case', pattern='*_sta.py')
	runner.run(discover)
	fp.close() # 关闭生成的报告