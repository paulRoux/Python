from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://baidu.com")

try:
    element = wait.until(
        EC.presence_of_element_located(
            (By.ID, "kw")
        )
    )
    print(element)
except TimeoutError:
    pass