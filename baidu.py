# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome() #获得浏览器对象
# driver = webdriver.Firefox() #获得浏览器对象
# driver = webdriver.Ie() #获得浏览器对象
driver.get("http://www.baidu.com") #向浏览器发送网址（URL）

# print("设置浏览器宽480、高800显示")
# driver.set_window_size(480, 800) # 设置为480时“百度一下按钮被遮挡，造成错误”
driver.maximize_window() # 设置浏览器全屏显示


driver.find_element_by_id("kw").send_keys("Selenium2") #在输入框中键盘输入“Selenium”
driver.find_element_by_id("su").click() #点击“百度一下”搜索按钮

driver.get("http://news.baidu.com")
driver.refresh() #刷新当前页面
driver.back() #浏览器后退
driver.forward() #浏览器前进

driver.quit() #退出并关闭浏览器
