class Page(object):
	'''
	页面基础类，用于所有页面的继承
	'''

	ourebuy_url = 'http://www.ourebuy.com'

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

	def switch_to_current_window(self):
		all_handles = self.driver.window_handles

		current_windows = self.driver.current_window_handle
		for handle in all_handles:
			if handle != current_windows:
				self.driver.switch_to.window(handle)