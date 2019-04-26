from selenium import webdriver


proxy ="http://ip:port"

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server={}".format(proxy))


# 可以用httpbin.org查看
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://baidu.com")