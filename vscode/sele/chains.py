from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://baidu.com")

inputTag = driver.find_element_by_id("kw")
submitTag = driver.find_element_by_id("su")

actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag)
actions.move_to_element(submitTag)
actions.click()
actions.perform()