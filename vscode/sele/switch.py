from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://baidu.com")

driver.execute_script("window.open('https://www.douban.com')")
print(driver.current_url)

driver.switch_to_window(driver.window_handles[1])
print(driver.current_url)

print(driver.window_handles)