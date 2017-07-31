from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from .entryMarketPage import entryMarket

class modityOrder(Page):
	'''
	供应商洽谈订单
	'''
	url = '/'

	market_link_loc = (By.LINK_TEXT, "网上超市")
	seller_home_loc = (By.LINK_TEXT, "卖方中心")

	commerce_order = (By.LINK_TEXT, "销售订单")
	commerce_suspense_order = (By.LINK_TEXT, "待处理订单")

	freight_input_loc = (By.ID, "yfamt_0")
	submit_order_btn_loc = (By.LINK_TEXT, "确认订单")
	note_input_loc = (By.ID, "gysbeiz")

	# 进入卖家中心
	def entry_home(self):
		ActionChains(self.driver).move_to_element(self.find_element(*self.market_link_loc)).perform()
		self.find_element(*self.seller_home_loc).click()

	# 卖方查看销售订单-待处理订单
	def check_order(self):
		self.find_element(*self.commerce_order).click()
		self.find_element(*self.commerce_suspense_order).click()

	# 返回订单号为order_id的订单所处的行号
	def check_order_index(self):
		order_id = self.find_orderID()
		tema = self.driver.find_elements_by_css_selector("body div.mainbody div div.fr.mrgT30.commerce_right div.contract_m.clearfix table tr td:nth-child(2) a")
		for i, item in enumerate(tema):
			if item.text == order_id:
				return i

	# 返回订单号为order_id的订单状态
	def check_order_state(self):
		i = self.check_order_index()
		state_a = self.driver.find_elements_by_css_selector("body div.mainbody div div.fr.mrgT30.commerce_right div.contract_m.clearfix table tr:nth-child(%s) td:nth-child(8) em" % (i+2))
		return state_a[0].text

	# 洽谈订单
	def click_modity_order_btn(self):
		i = self.check_order_index()

		#将页面滚动到底部
		self.window_to_bottom()
		
		btn_a = self.driver.find_elements_by_css_selector("body div.mainbody div div.fr.mrgT30.commerce_right div.contract_m.clearfix table tr:nth-child(%s) td.modity_td p a.modity_tda" % (i+2))
		btn_a[0].click()

	# 确认订单
	def submit_order(self, freight, note):
		self.find_element(*self.freight_input_loc).send_keys(freight)
		self.find_element(*self.note_input_loc).send_keys(note)
		self.find_element(*self.submit_order_btn_loc).click()
		self.driver.switch_to_alert().accept()
		self.click_ok_btn()

	def entry_home_check_order(self):
		# 进入网上超市个人中心
		entryMarket(self.driver).entry_market("seller")

		# 进入卖家中心查看订单
		self.entry_home()
		self.check_order()

	# 洽谈订单
	def modity_order(self):
		self.click_modity_order_btn()

		self.submit_order(5, "无备注")