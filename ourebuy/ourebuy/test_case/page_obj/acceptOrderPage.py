from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from .entryMarketPage import entryMarket

class acceptOrder(Page):
	'''
	结算商接受订单
	'''
	url = '/'

	commerce_order = (By.LINK_TEXT, "销售订单")
	commerce_accept_order = (By.LINK_TEXT, "待接受订单")
	commerce_suspense_order = (By.LINK_TEXT, "待处理订单")

	accept_btn_loc = (By.LINK_TEXT, "接受")
	ok_btn_frame_loc = (By.XPATH, "/html/body/div[4]/div[2]/iframe")
	ok_btn_loc = (By.XPATH, "/html/body/div/div/div/button")

	# 结算商查看销售订单-待接受订单
	def check_accept_order(self):
		self.find_element(*self.commerce_order).click()
		self.find_element(*self.commerce_accept_order).click()

	# 结算商查看销售订单-待处理订单
	def check_suspense_order(self):
		self.find_element(*self.commerce_suspense_order).click()

	# 返回订单号为order_id的订单所处的行号
	def check_order_index(self, orderid_td_i):
		order_id = self.find_orderID()
		tema = self.driver.find_elements_by_css_selector("#right div div.contract_m.clearfix div:nth-child(1) table tbody tr td:nth-child(%s) a" % orderid_td_i)
		for i, item in enumerate(tema):
			if item.text == order_id+"-S":
				return i

	# 返回订单号为order_id的订单状态
	def check_order_state(self, orderid_td_i, state_td_i):
		i = self.check_order_index(orderid_td_i)
		state_a = self.driver.find_elements_by_css_selector("#right div div.contract_m.clearfix div:nth-child(1) table tbody tr:nth-child(%s) td:nth-child(%s) em" % (i+1, state_td_i))
		return state_a[0].text

	def entry_home_check_order(self):
		# 进入网上超市个人中心
		entryMarket(self.driver).entry_market("middleman")

		# 查看待接受订单
		self.check_accept_order()

	# 接受订单
	def accept_order(self):
		i = self.check_order_index(2)

		#将页面滚动到底部
		self.window_to_bottom()
		
		btn_a = self.driver.find_elements_by_css_selector("#right div div.contract_m.clearfix div:nth-child(1) table tbody tr:nth-child(%s) td.modity_td p a:nth-child(2)" % (i+1))
		btn_a[0].click()

		sleep(1)

		self.find_element(*self.accept_btn_loc).click()

		sleep(1)
		self.driver.switch_to.frame(self.find_element(*self.ok_btn_frame_loc))
		self.find_element(*self.ok_btn_loc).click()


