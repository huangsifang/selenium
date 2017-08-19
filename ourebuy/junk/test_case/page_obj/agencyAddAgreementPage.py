from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

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
	time_ok_loc = (By.ID, "dpOkInput")

	lower_price_loc = (By.ID, "targetprice")
	is_make_sure_loc = (By.XPATH, "//*[@id='gform']/div/div[2]/div[1]/p[1]/input[3]")
	number_loc = (By.ID, "sl")
	unit_loc = (By.ID, "sldw")
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
	addr_province_option_loc = (By.XPATH, "//*[@id='dq1code']/option[[@value='浙江省']")
	addr_city_select_loc = (By.ID, "dqcode")
	addr_city_option_loc = (By.XPATH, "//*[@id='dqcode']/option[[@value='杭州市']")
	addr_specific_loc = (By.ID, "copadde")

	seller_choose_loc = (By.XPATH, "//*[@id='gform']/div/div[2]/div[6]/p[1]/span/span/span")
	seller_choose_frame_loc = (By.XPATH, "/html/body/div[8]/div/iframe")
	seller_find_loc = (By.ID, "mbname")
	seller_find_btn_loc = (By.XPATH, "//*[@id='queryForm']/div[1]/input[2]")
	seller_ok_loc = (By.XPATH, "//*[@id='queryForm']/div[4]/ul/li[1]/a")

	save_btn = (By.XPATH, "//*[@id='gform']/div/div[2]/div[7]/a[1]")

	# 从文件读取信息
	def read_file(self):
		try:
			data = csv.reader(open('junk/data/agreement.csv', 'r'))
			return data[1]
		except FileNotFoundError:
			print("未找到文件")

	def choose_time(self):
		self.switch_to.frame(self.find_element(*self.time_frame_loc))
		self.find_element(*self.time_minute_input_loc).click()
		self.driver.find_element_by_id("kw").send_keys(Keys.ARROW_RIGHT)
		self.find_element(*self.time_ok_loc).click()
		self.driver.switch_to.default_content() 

	# 新增委托协议
	def add_agreement(self):
		data = self.read_file()
		self.find_element(*self.man_name_loc).send_keys(data[0])
		self.find_element(*self.tel_loc).send_keys(data[1])

		self.find_element(*self.start_time_loc).click()
		self.choose_time()

		self.find_element(*self.end_time_loc).click()
		self.choose_time()

		self.find_element(*self.lower_price_loc).send_keys(data[2])
		self.find_element(*self.number_loc).send_keys(data[3])
		self.find_element(*self.unit_loc).click()
		self.find_element(*self.product_name_chinese_loc).send_keys(data[4])
		self.find_element(*self.product_name_english_loc).send_keys(data[5])
		self.find_element(*self.product_model_loc).send_keys(data[6])
		self.find_element(*self.product_size_loc).send_keys(data[7])
		self.find_element(*self.product_standard_loc).send_keys(data[8])
		self.find_element(*self.addr_specific_loc).send_keys(data[11])


	def agency_add_agreement(self):
		self.entry_menu("新增委托协议", "我的受托协议")
		self.find_element(*self.choose_item_loc).click()
		self.find_element(*self.next_loc).click()
		sleep(1)

		# 新增委托协议
		self.add_agreement()
