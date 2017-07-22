from selenium import webdriver  
import time  
  
driver = webdriver.Chrome()  
driver .get("http://www.126.com")  
  
print("Before login.........")  
  
#打印当前页面title  
title=driver.title  
print(title)  
  
#打印当前页面URL  
now_url =driver.current_url  
print(now_url)  
  
#执行邮箱登陆  
driver.switch_to.frame(driver.find_element_by_id("x-URS-iframe"))  
driver.find_element_by_name("email").clear()  
driver.find_element_by_name("email").send_keys("username")  
driver.find_element_by_name("password").clear()  
driver.find_element_by_name("password").send_keys("password")  
driver.find_element_by_id("dologin").click()  
driver.switch_to.default_content()  
  
time.sleep(5)  
print("After login......")  
  
  
#再次打印当前页面title  
title=driver.title  
print(title)  
  
#打印当前页面URL  
now_url=driver.current_url  
print(now_url)  
  
#获得登陆的用户名  
#user =driver.find_element_by_name('email').text  
user=driver.find_element_by_id ('spnUid').text  
print(user)  
  
#driver.quit ()
