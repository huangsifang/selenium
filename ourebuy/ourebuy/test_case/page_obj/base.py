from time import sleep
from selenium.webdriver.common.by import By

class Page(object):
	'''
	页面基础类，用于所有页面的继承
	'''

	ourebuy_url = 'http://www.ourebuy.com'

	ok_btn_loc = (By.XPATH, "/html/body/div[6]/div/span[3]/a[1]")

	'''
	def __new__(cls, selenium_driver, base_url=ourebuy_url, parent=None):  
		if not hasattr(cls, '_instance'):  
			orig = super(Page, cls)  
			cls._instance = orig.__new__(cls)
		return cls._instance
	'''

	def __init__(self, selenium_driver, base_url=ourebuy_url, parent=None):
		self.base_url = base_url
		self.driver = selenium_driver
		self.timeout = 30
		self.parent = parent

	def _open(self, url):
		url = self.base_url + url
		self.driver.get(url)
		assert self.on_page(),'Did not land on %s' % url

	def find_element(self, *loc):
		return self.driver.find_element(*loc)

	def find_elements(self, *loc):
		return self.driver.find_elements(*loc)

	def open(self):
		self._open(self.url)

	def on_page(self):
		return self.driver.current_url == (self.base_url + self.url)

	def script(self, src):
		return self.driver.execute_script(src)

	# 切换到当前页面
	def switch_to_current_window(self):
		all_handles = self.driver.window_handles

		current_windows = self.driver.current_window_handle
		for handle in all_handles:
			if handle != current_windows:
				self.driver.switch_to.window(handle)

	# 进入点击侧边栏条目
	def entry_menu(self, sub_menu, menu = None):
		if menu != None:
			self.find_element(*(By.LINK_TEXT, menu)).click()
		self.find_element(*(By.LINK_TEXT, sub_menu)).click()

	# 从文件中读取最后一个订单号
	def find_orderID(self):
		try:
			orderID_file = open("ourebuy/data/orderID.txt", 'r')
			lines = orderID_file.readlines()
			orderID_file.close()
			if lines[-1][-1:] == '\n': # 存在回车符
				orderID = lines[-1][:-1]
			else: # 不存在
				orderID = lines[-1]
			return orderID
		except FileNotFoundError:
			print("未找到文件")

	# 从文件中读取最后一个协议号
	def find_agreementID(self):
		try:
			agreementID_file = open("junk/data/agreementID.txt", 'r')
			lines = agreementID_file.readlines()
			agreementID_file.close()
			if lines[-1][-1:] == '\n': # 存在回车符
				agreementID = lines[-1][:-1]
			else: # 不存在
				agreementID = lines[-1]
			return agreementID
		except FileNotFoundError:
			print("未找到文件")

	#将页面滚动到底部
	def window_to_bottom(self):
		js="window.scrollTo(0,document.body.scrollHeight)"
		self.driver.execute_script(js)
		sleep(1)

	# 弹出框确定按钮
	def click_ok_btn(self):
		self.find_element(*self.ok_btn_loc).click()