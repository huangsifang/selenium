from threading import Thread
from selenium.webdriver import Remote
from selenium import webdriver

'''
# part3
global drivers
drivers = []
'''

# 启动浏览器驱动
def browser():
	# driver = webdriver.Chrome()
	host = '192.168.2.78:4444' # 运行主机：端口号
	dc = {'browserName': 'chrome'} # 指定浏览器
	driver = Remote(command_executor='http://' + host + '/wd/hub', desired_capabilities=dc)

	'''
	dc = {'browserName': browser}
	driver = webdriver.Remote(command_executor=host, desired_capabilities=dc)
	'''



	'''
	# 启动参数（指定运行主机与浏览器）
	lists = {'http://192.168.2.78:4444/wd/hub': 'chrome',
			'http://192.168.2.78:5555/wd/hub': 'internet explorer'
			}
	# drivers = []

	for host, browser in lists.items():
		print(host, browser)
		dc = {'browserName': browser}
		driver = webdriver.Remote(command_executor=host, desired_capabilities=dc)
		drivers.append(driver)
	'''


	return driver


'''
def test_baidu(host, browser):
	print(host, browser)
	driver = browser_init(host, browser)
	driver.get("http://www.baidu.com")
	driver.close()
'''


'''
def test_baidu(i):
	drivers[i].get("http://www.baidu.com")
	drivers[i].quit()
'''


if __name__ == '__main__':
	dr = browser()
	dr.get("http://www.baidu.com")
	dr.quit()

	'''
	# 启动参数（指定运行主机与浏览器）
	lists = {'http://192.168.2.78:4444/wd/hub': 'chrome',
			'http://192.168.2.78:5555/wd/hub': 'internet explorer'
			}
	threads = []
	files = range(len(lists))

	# 创建线程
	for host, browser in lists.items():
		t = Thread(target=test_baidu, args=(host, browser))
		threads.append(t)

	# 启动线程
	for i in files:
		threads[i].start()
	for i in files:
		threads[i].join()
	'''



	'''
	drivers = browser()
	files = range(len(drivers))
	threads = []

	# 创建线程
	for i in files:
		t = Thread(target=test_baidu, args=(i))
		threads.append(t)

	# 启动线程
	for i in files:
		threads[i].start()
	for i in files:
		threads[i].join()
	'''