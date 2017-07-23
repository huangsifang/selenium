from selenium import webdriver
# 引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.hao123.com/")
driver.maximize_window() # 设置浏览器全屏显示

# 定位到要右击的元素
el = driver.find_element_by_css_selector("#slidetoolbarContainer .applist div:nth-child(2)")
# 对定位到的元素执行鼠标右键操作
# ActionChains(driver).context_click(el).perform()

# 鼠标悬停
ActionChains(driver).move_to_element(el).perform()

# 双击操作
# ActionChains(driver).doule_click(el).perform()

# 拖放操作
# ActionChains(driver).drag_and_drop(element, target).perform()
