from selenium import webdriver
# 引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("http://c-t.yunpan.360.cn/my/index/")
'''
driver.find_element_by_css_selector("[name='account']").send_keys("17816869682")
driver.find_element_by_css_selector("[name='password']").send_keys("a65332794")
driver.find_element_by_css_selector("[type='submit']")
'''

# 定位到要右击的元素
right_click = driver.find_element_by_css_selector("#list li:first-child")
# 对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right_click).perform()
