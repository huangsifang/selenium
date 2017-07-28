from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from .entryMarketPage import entryMarket

class addDraft(Page):
	'''
	用户新增汇票
	'''
	url = '/'

	add_draft_btn_loc = (By.ID, "addhp")
	add_btn_loc = (By.LINK_TEXT, "新增")

	draft_date_year = (By.ID, "yearStr")
	draftID_input_loc = (By.ID, "billno")
	payee_select_loc = (By.ID, "sknames")
	payee_option_loc = (By.XPATH, "//*[@id='sknames']/option[48]")


	# 买方承兑汇票管理-承兑汇票管理
	def entry_draft_manage(self):
		self.find_element(*(By.LINK_TEXT, "承兑汇票管理")).click()
		self.find_element(*(By.XPATH, "/html/body/div[3]/div/div[1]/div/ul/li[2]/dl/dd[1]/a")).click()

	# 填写汇票信息
	def fill_draft(self):
		# 日期
		self.find_element(*self.draft_date_year).click()
		sleep(1)
		date = self.driver.find_elements_by_css_selector("body div div:nth-child(3) table tbody tr:nth-child(2) td:nth-child(1)")
		date.click()

		# 票号
		self.find_element(*self.draftID_input_loc).send_keys("2017072811111111")

		# 收款人
		self.find_element(*self.payee_select_loc).click()
		self.find_element(*self.payee_option_loc).click()


	# 返回订单号为order_id的订单状态
	def check_order_state(self, order_id):
		tema = self.driver.find_elements_by_css_selector("body div.mainbody div div.fr.mrgT30.commerce_right div div.contract_m.clearfix table tr td:nth-child(2) a")
		for i, item in enumerate(tema):
			if item.text == order_id:
				state_a = self.driver.find_elements_by_css_selector("body div.mainbody div div.fr.mrgT30.commerce_right div div.contract_m.clearfix table tr:nth-child(%s) td:nth-child(8) em" % (i+2))
				return state_a[0].text

	def add_draft(self):
		# 进入网上超市个人中心
		entryMarket(self.driver).entry_market("buyer")

		# 买方采购订单-待处理订单
		# self.entry_menu("待处理订单", "采购订单")

		# 买方承兑汇票管理-承兑汇票管理
		self.entry_draft_manage()

		self.window_to_bottom()

		# 新增汇票
		self.find_element(*self.add_draft_btn_loc).click()
		self.find_element(*self.add_btn_loc).click()

		sleep(1)
		# self.fill_draft()