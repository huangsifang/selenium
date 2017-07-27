from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from .entryMarketPage import entryMarket

class buy(Page):
	'''
	用户购买商品
	'''
	url = '/'

	buy_consumer_goods_loc = (By.XPATH, "//*[@id='head_nn']/li[1]/a")
	buy_computer_goods_loc = (By.XPATH, "//*[@id='head_nn']/li[1]/dl/dd[1]/h3/a")
	buy_notebook_goods_loc = (By.XPATH, "//*[@id='head_nn']/li[1]/dl/dd[1]/div/div/div[1]/div/p/a")
	buy_a_computer_loc = (By.ID, "bigPic")

	search_input_loc = (By.ID, "title")
	search_btn = (By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/input[2]")
	buy_a_computer_loc2 = (By.XPATH, "//*[@id='gform2']/div[1]/ul/li/div/a/img")

	ticket_pay_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[2]/div[4]/div/dl/dd[2]/a")
	buy_now_btn = (By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[2]/div[9]/div/a[1]")
	submit_btn = (By.ID, "submit_btn")

	market_link_loc = (By.LINK_TEXT, "网上超市")
	buyer_home_loc = (By.LINK_TEXT, "买方中心")

	buyer_order = (By.LINK_TEXT, "采购订单")
	buyer_suspense_order = (By.LINK_TEXT, "待处理订单")

	# 通过导航栏找到计算机0000商品
	def nav_to_goods(self):
		# 消费类商品--计算机--笔记本
		ActionChains(self.driver).move_to_element(self.find_element(*self.buy_consumer_goods_loc)).perform()
		sleep(1)
		ActionChains(self.driver).move_to_element(self.find_element(*self.buy_computer_goods_loc)).perform()
		sleep(1)
		self.find_element(*self.buy_notebook_goods_loc).click()
		sleep(1)

		# 点击计算机0000商品
		self.find_element(*self.buy_a_computer_loc).click()
		self.switch_to_current_window()

	# 通过搜索找到商品
	def search_to_goods(self, good_name):
		self.find_element(*self.search_input_loc).send_keys(good_name)
		self.find_element(*self.search_btn).click()

		# 点击第一个商品
		self.find_element(*self.buy_a_computer_loc2).click()
		self.switch_to_current_window()

	# 立即购买
	def buy_a_good(self):
		self.find_element(*self.ticket_pay_loc).click()
		self.find_element(*self.buy_now_btn).click()
		self.find_element(*self.submit_btn).click()

		self.driver.switch_to_alert().accept()

	# 返回买方中心
	def entry_home(self):
		ActionChains(self.driver).move_to_element(self.find_element(*self.market_link_loc)).perform()
		self.find_element(*self.buyer_home_loc).click()

	# 买方查看订单
	def check_order(self):
		self.find_element(*self.buyer_order).click()
		self.find_element(*self.buyer_suspense_order).click()

	# 返回订单号为order_id的订单状态
	def check_order_state(self, order_id):
		tema = self.driver.find_elements_by_css_selector("body div.mainbody div div.fr.mrgT30.commerce_right div div.contract_m.clearfix table tr td:nth-child(2) a")
		for i, item in enumerate(tema):
			if item.text == order_id:
				state_a = self.driver.find_elements_by_css_selector("body div.mainbody div div.fr.mrgT30.commerce_right div div.contract_m.clearfix table tr:nth-child(%s) td:nth-child(8) em" % (i+2))
				return state_a[0].text

	def buy(self):
		# 进入网上超市个人中心
		entryMarket(self.driver).entry_market("buyer")

		# 通过导航栏找到计算机0000商品
		# self.nav_to_goods()

		# 通过搜索找到计算机0000商品
		self.search_to_goods("计算机0000")

		# 购买商品
		self.buy_a_good()

		current_url = self.driver.current_url
		# 截取url等号后面的字符（订单号）
		self.current_order_id = current_url.split("=")[-1]
		print("订单号: %s" % self.current_order_id)

		# 返回买家中心查看商品
		self.entry_home()
		self.check_order()