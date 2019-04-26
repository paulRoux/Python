from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://baidu.com")


for cookie in driver.get_cookies():
    print(cookie)

# 获取某个key的cookie
driver.get_cookie("")

# 删除某个cookie
driver.delete_cookie("")