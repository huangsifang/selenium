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
	payee_option_loc = (By.XPATH, "//*[@id='sknames']/option[@value='浙江杭州高达票据测试专用结算商一']")
	payee_account_loc = (By.ID, "skno")
	payee_bank_loc = (By.ID, "skbank")
	money_loc = (By.ID, "amtStr")
	money_input_loc = (By.ID, "amt")
	money_ok_btn_loc = (By.XPATH, "//*[@id='gform']/div/div[1]/div[2]/div[2]/em")
	remit_end_date_loc = (By.ID, "endrqStr")
	contract_num_loc = (By.ID, "billhthm")
	deposit_bank_num_loc = (By.ID, "bankno")
	deposit_bank_addr_loc = (By.ID, "bankaddr")
	acceptor_select_loc = (By.ID, "acceptor")
	acceptor_option_loc = (By.XPATH, "//*[@id='acceptor']/option[@value='高达软件']")

	ok_end_fill_btn_loc = (By.XPATH, "//*[@id='gform']/div/div[2]/a[2]")

	final_ok_btn_loc = (By.LINK_TEXT, "确认登记完毕")

	# 票号
	draft_id = "2017073111111119"

	# 返回订单号为order_id的订单所处的行号
	def check_order_index(self):
		order_id = self.find_orderID()
		tema = self.driver.find_elements_by_css_selector("body div.mainbody div div.fr.mrgT30.commerce_right div div.contract_m.clearfix table tbody tr td:nth-child(2) a")
		for i, item in enumerate(tema):
			if item.text == order_id:
				return i

	# 返回订单号为order_id的订单状态
	def check_order_state(self):
		i = self.check_order_index()
		state_em = self.driver.find_elements_by_css_selector("body > div.mainbody > div > div.fr.mrgT30.commerce_right > div > div.contract_m.clearfix > table > tbody > tr:nth-child(%s) > td:nth-child(8) > em" % (i+2))
		return state_em[0].text

	# 点击登记承兑汇票
	def login_draft(self):
		i = self.check_order_index()
		login_draft_btn = self.driver.find_elements_by_css_selector("body > div.mainbody > div > div.fr.mrgT30.commerce_right > div > div.contract_m.clearfix > table > tbody > tr:nth-child(%s) > td.modity_td > p > a.regSettle" % (i+2))
		login_draft_btn[0].click()

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
		self.find_element(*self.draftID_input_loc).send_keys(self.draft_id)

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

		# 承兑人
		self.find_element(*self.acceptor_select_loc).click()
		self.find_element(*self.acceptor_option_loc).click()

		self.find_element(*self.ok_end_fill_btn_loc).click()

		self.driver.switch_to_alert().accept()


	# 返回票号为draft_id的票所处的行号
	def check_draft_index(self):
		tema = self.driver.find_elements_by_css_selector("#gform > div:nth-child(2) > div.fl > table > tbody > tr > td:nth-child(4)")
		for i, item in enumerate(tema):
			if item.text ==self. draft_id:
				return i

	# 返回票号为draft_id的票状态
	def check_draft_state(self):
		i = self.check_draft_index()
		state_span = self.driver.find_elements_by_css_selector("#gform > div:nth-child(2) > div:nth-child(2) > table > tbody > tr:nth-child(%s) > td:nth-child(1) > span" % (i+2))
		return state_span[0].text

	# 提交汇票
	def submit_draft(self):
		i = self.check_draft_index()
		submit_a = self.driver.find_elements_by_css_selector("#gform > div:nth-child(2) > div:nth-child(2) > table > tbody > tr:nth-child(%s) > td.opt > a:nth-child(1)" % (i+2))
		submit_a[0].click()
		self.driver.switch_to_alert().accept()
		self.click_ok_btn()

	def entry_order(self):
		# 进入网上超市个人中心
		entryMarket(self.driver).entry_market("buyer")

		# 买方采购订单-待处理订单
		self.entry_menu("待处理订单", "采购订单")

	def entry_draft(self):
		# 进入网上超市个人中心
		entryMarket(self.driver).entry_market("buyer")

		# 买方承兑汇票管理-承兑汇票管理
		self.entry_draft_manage()

	def add_draft(self):
		self.window_to_bottom()

		# 新增汇票
		self.find_element(*self.add_draft_btn_loc).click()
		self.find_element(*self.add_btn_loc).click()

		sleep(1)
		self.fill_draft()

		self.find_element(*self.final_ok_btn_loc).click()
		self.driver.switch_to_alert().accept()

		ok_btn = self.driver.find_elements_by_css_selector("body > div.xubox_layer.xubox_layer_0 > div > span.xubox_botton > a.xubox_yes.xubox_botton1_0")
		ok_btn[0].click()