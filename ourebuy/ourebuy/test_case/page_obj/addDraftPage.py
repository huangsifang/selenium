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

	draft_frame_loc = (By.XPATH, "/html/body/div[7]/div/iframe")
	draft_date_year_loc = (By.ID, "yearStr")
	draft_date_frame_loc = (By.ID, "_iframe_wdatepicker")
	draft_nowadays_loc = (By.ID, "dpTodayInput")
	draftID_input_loc = (By.ID, "billno")
	drawee_account_loc = (By.ID, "fkno")
	drawee_bank_loc = (By.ID, "fkbank")
	payee_select_loc = (By.ID, "sknames")
	payee_option_loc = (By.XPATH, "//*[@id='sknames']/option[48]")
	payee_account_loc = (By.ID, "skno")
	payee_bank_loc = (By.ID, "skbank")
	money_loc = (By.ID, "amtStr")
	money_input_loc = (By.ID, "amt")
	money_ok_btn_loc = (By.XPATH, "//*[@id='gform']/div/div[1]/div[2]/div[2]/em")
	remit_end_date_loc = (By.ID, "endrqStr")
	contract_num_loc = (By.ID, "billhthm")
	deposit_bank_num_loc = (By.ID, "bankno")
	deposit_bank_addr_loc = (By.ID, "bankaddr")

	ok_end_fill_btn_loc = (By.XPATH, "//*[@id='gform']/div/div[2]/a[2]")

	final_ok_btn_loc = (By.LINK_TEXT, "确认登记完毕")

	# 买方承兑汇票管理-承兑汇票管理
	def entry_draft_manage(self):
		self.find_element(*(By.LINK_TEXT, "承兑汇票管理")).click()
		self.find_element(*(By.XPATH, "/html/body/div[3]/div/div[1]/div/ul/li[2]/dl/dd[1]/a")).click()

	# 填写汇票信息
	def fill_draft(self):
		self.driver.switch_to.frame(self.find_element(*self.draft_frame_loc))

		# 日期
		self.find_element(*self.draft_date_year_loc).click()
		self.driver.switch_to.default_content()
		sleep(1)
		self.driver.switch_to.frame(self.find_element(*self.draft_date_frame_loc))
		self.find_element(*self.draft_nowadays_loc).click()
		self.driver.switch_to.default_content()

		self.driver.switch_to.frame(self.find_element(*self.draft_frame_loc))

		# 票号
		self.find_element(*self.draftID_input_loc).send_keys("2017072811111111")

		# 付款人
		self.find_element(*self.drawee_account_loc).send_keys("1")
		self.find_element(*self.drawee_bank_loc).send_keys("1")

		# 收款人
		self.find_element(*self.payee_select_loc).click()
		self.find_element(*self.payee_option_loc).click()
		self.find_element(*self.payee_account_loc).send_keys("1")
		self.find_element(*self.payee_bank_loc).send_keys("1")

		# 出票金额
		self.find_element(*self.money_loc).click()
		self.find_element(*self.money_input_loc).send_keys("1")
		self.find_element(*self.money_ok_btn_loc).click()

		# 汇款到期日
		self.find_element(*self.remit_end_date_loc).click()
		self.driver.switch_to.default_content()
		sleep(1)
		self.driver.switch_to.frame(self.find_element(*self.draft_date_frame_loc))
		last_day = self.driver.find_elements_by_css_selector("body > div > div:nth-child(3) > table > tbody > tr:nth-child(7) > td:nth-child(7)")
		last_day[0].click()
		self.driver.switch_to.default_content()

		self.driver.switch_to.frame(self.find_element(*self.draft_frame_loc))

		# 交易合同号码
		self.find_element(*self.contract_num_loc).send_keys("1")

		# 付款人开户行
		self.find_element(*self.deposit_bank_num_loc).send_keys("1")
		self.find_element(*self.deposit_bank_addr_loc).send_keys("1")

		self.find_element(*self.ok_end_fill_btn_loc).click()

		self.driver.switch_to_alert().accept()


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
		self.fill_draft()

		self.find_element(*self.final_ok_btn_loc).click()
		self.driver.switch_to_alert().accept()