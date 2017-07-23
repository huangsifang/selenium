from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()

# 打开上传功能页面
file_path = 'file://' + os.path.abspath('upfile.html')
driver.get(file_path)
driver.maximize_window() # 设置浏览器全屏显示

# driver.find_element_by_name("file").send_keys('E:\\downloads\2.zip')

driver.find_element_by_name("file").click()

os.system("E:\\selenium\\upfile.exe")

sleep(5)

driver.quit()
