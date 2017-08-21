from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base import Page
from time import sleep
import csv
import re

class agencyAddAgreement(Page):
	'''
	中介新增协议
	'''

	url = '/'

	choose_item_loc = (By.ID, "16")
	next_loc = (By.ID, "sub")

	man_name_loc = (By.ID, "contacts")
	tel_loc = (By.ID, "phone")

	start_time_loc = (By.ID, "startdateStr")
	end_time_loc = (By.ID, "enddateStr")
	time_frame_loc = (By.ID, "_iframe_wdatepicker")
	time_minute_input_loc = (By.XPATH, "//*[@id='dpTime']/table/tbody/tr[1]/td[1]/input[3]")
	time_end_loc = (By.XPATH, "/html/body/div/div[3]/table/tbody/tr[7]/td[5]")
	time_ok_loc = (By.ID, "dpOkInput")

	lower_price_loc = (By.ID, "targetprice")
	no_need_check_loc = (By.XPATH, "//*[@id='gform']/div/div[2]/div[1]/p[1]/input[3]")
	number_loc = (By.ID, "sl")
	unit_input_loc = (By.ID, "sldw")
	unit_frame_loc = (By.ID, "__ieselect")
	unit_loc = (By.XPATH, "//*[@id='iframediv']/div[2]")
	product_name_chinese_loc = (By.ID, "pmc")
	product_name_english_loc = (By.ID, "pme")
	product_model_loc = (By.ID, "cz")
	product_size_loc = (By.ID, "gg")
	product_standard_loc = (By.ID, "bz")

	issuance_start_data_input_loc = (By.ID, "fhrq1")
	issuance_end_data_input_loc = (By.ID, "fhrq2")
	issuance_start_data_loc = (By.XPATH, "/html/body/div/div[3]/table/tbody/tr[7]/td[6]")
	issuance_end_data_loc = (By.XPATH, "/html/body/div/div[3]/table/tbody/tr[7]/td[7]")

	addr_province_select_loc = (By.ID, "dq1code")
	addr_province_option_loc = (By.XPATH, "//*[@id='dq1code']/option[@value='330000']")
	addr_city_select_loc = (By.ID, "dqcode")
	addr_city_option_loc = (By.XPATH, "//*[@id='dqcode']/option[@value='330100']")
	addr_specific_loc = (By.ID, "copadde")

	seller_choose_loc = (By.XPATH, "//*[@id='gform']/div/div[2]/div[6]/p[1]/span/span/span")
	seller_choose_frame_loc = (By.XPATH, "/html/body/div[8]/div/iframe")
	seller_find_loc = (By.ID, "mbname")
	seller_find_btn_loc = (By.XPATH, "//*[@id='queryForm']/div[1]/input[2]")
	seller_ok_loc = (By.XPATH, "//*[@id='queryForm']/div[4]/ul/li[1]/a")

	save_btn = (By.XPATH, "//*[@id='gform']/div/div[2]/div[7]/a[1]")

	final_ok_btn = (By.XPATH, "/html/body/div[7]/div/span[3]/a[1]")

	agreement_id_loc = (By.XPATH, "/html/body/div[7]/div/span[2]")

	# 从文件读取信息
	def read_file(self):
		try:
			data = csv.reader(open('junk/data/agreement.csv', 'r'))
			rows = [row for row in data]
			return rows[1] # 返回第二行
		except FileNotFoundError:
			print("未找到文件")

	# 返回协议号为agreement_id的协议所处的行号
	def check_agreement_index(self, agreement_id_i):
		agreement_id = self.find_agreementID()
		tema = self.driver.find_elements_by_css_selector("body div.mainbody div div.fr.mrgT30.commerce_right div.purchbidding_table.quote_table1 table tbody tr td:nth-child(%s) p:nth-child(1) a" % agreement_id_i)
		for i, item in enumerate(tema):
			if item.text == agreement_id+"-S":
				return i

	# 返回协议号为agreement_id的协议状态
	def check_agreement_state(self, agreement_id_td_i, state_td_i):
		i = self.check_agreement_index(agreement_id_td_i)
		state_a = self.driver.find_elements_by_css_selector("body div.mainbody div div.fr.mrgT30.commerce_right div.purchbidding_table.quote_table1 table tbody tr:nth-child(%s) td:nth-child(%s) p:nth-child(1) a" % (i+1, state_td_i))
		return state_a[0].text

	def choose_time(self, type):
		self.driver.switch_to.frame(self.find_element(*self.time_frame_loc))
		if type == "start":
			self.find_element(*self.time_minute_input_loc).send_keys(Keys.ARROW_RIGHT)
		else:
			self.find_element(*self.time_end_loc).click()
		self.find_element(*self.time_ok_loc).click()
		self.driver.switch_to.default_content() 

	def choose_issuance_date(self, type):
		self.driver.switch_to.frame(self.find_element(*self.time_frame_loc))
		if type == "start":
			self.find_element(*self.issuance_start_data_loc).click()
		else:
			self.find_element(*self.issuance_end_data_loc).click()
		self.driver.switch_to.default_content()

	# 新增委托协议
	def add_agreement(self):
		data = self.read_file()
		self.find_element(*self.man_name_loc).send_keys(data[0])
		self.find_element(*self.tel_loc).send_keys(data[1])

		self.find_element(*self.start_time_loc).click()
		self.choose_time("start")

		self.find_element(*self.end_time_loc).click()
		self.choose_time("end")

		self.find_element(*self.lower_price_loc).send_keys(data[2])
		self.find_element(*self.no_need_check_loc).click()
		self.find_element(*self.number_loc).send_keys(data[3])
		self.find_element(*self.unit_input_loc).click()
		self.driver.switch_to.frame(self.find_element(*self.unit_frame_loc))
		self.find_element(*self.unit_loc).click()
		self.driver.switch_to.default_content()

		self.find_element(*self.product_name_chinese_loc).send_keys(data[4])
		self.find_element(*self.product_name_english_loc).send_keys(data[5])
		self.find_element(*self.product_model_loc).send_keys(data[6])
		self.find_element(*self.product_size_loc).send_keys(data[7])
		self.find_element(*self.product_standard_loc).send_keys(data[8])

		self.find_element(*self.issuance_start_data_input_loc).click()
		self.choose_issuance_date("start")
		
		self.find_element(*self.issuance_end_data_input_loc).click()
		self.choose_issuance_date("end")

		self.find_element(*self.addr_province_select_loc).click()
		self.find_element(*self.addr_province_option_loc).click()
		self.find_element(*self.addr_city_select_loc).click()
		self.find_element(*self.addr_city_option_loc).click()

		self.find_element(*self.addr_specific_loc).send_keys(data[11])

		self.find_element(*self.seller_choose_loc).click()
		self.driver.switch_to.frame(self.find_element(*self.seller_choose_frame_loc))
		self.find_element(*self.seller_find_loc).send_keys("废旧物资供应")
		self.find_element(*self.seller_find_btn_loc).click()
		self.find_element(*self.seller_ok_loc).click()
		self.find_element(*self.save_btn).click()

		self.save_agreement_id_to_file()

		# self.find_element(*self.final_ok_btn).click()

	def save_agreement_id_to_file(self):
		self.agreement_list = re.split(r'^[\[\]]+',self.find_element(*self.agreement_id_loc).text)
		print(self.agreement_list)
		self.current_agreement_id = self.agreement_list[1]
		print(self.current_agreement_id)
		# 将订单号写入文件中
		agreementID_file = open("junk/data/agreementID.txt", 'a')
		agreementID_file.write("%s\n" % self.current_agreement_id)
		agreementID_file.close()

	def send_to_seller(self):
		pass

	def agency_add_agreement(self):
		self.entry_menu("新增委托协议", "我的受托协议")
		self.find_element(*self.choose_item_loc).click()
		self.find_element(*self.next_loc).click()
		sleep(1)

		# 新增委托协议
		self.add_agreement()
