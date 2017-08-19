from selenium.webdriver import Remote
from selenium import webdriver

# 启动浏览器驱动
def browser():
	# driver = webdriver.Chrome()
	host = '192.168.2.78:4444' # 运行主机：端口号
	dc = {'browserName': 'chrome'} # 指定浏览器
	driver = Remote(command_executor='http://' + host + '/wd/hub', desired_capabilities=dc)
	return driver

if __name__ == '__main__':
	dr = browser()
	dr.get("http://www.baidu.com")
	dr.quit()