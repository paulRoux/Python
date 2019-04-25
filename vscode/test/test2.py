from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException
from time import sleep


url = ""

def chromeTest():
    url = "https://www.baidu.com"
    driver = webdriver.Chrome()
    driver.get(url)

    driver.find_elements_by_class_name("s_ipt").send_keys("人工智能")
    driver.find_element_by_class_name("btn_wr s_btn_wr bg").click()
    sleep(4)

    # 滚动条
    js = "document.documentElement.scrollTop=1000"
    driver.execute_script(js)

    driver.close()


def chromeWaitTest():
    url = "https://www.jd.com"
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 30)
    driver.get(url)

    try:
        input = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#key")
            )
        )
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#search > div > div.form > button")
            )
        )
        input[0].send_keys("人工智能")
        submit.click()

        total = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1) > b')
            )
        )

        # 滑动到底部，加载出后三十个货物信息
        while len(driver.find_element_by_class_name('gl-item')) < 60:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            sleep(2)

        html = driver.page_source
        print(html)
    except TimeoutException:
        chromeWaitTest()


def chromeHeaderless():
    url = "https://www.baidu.com"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    html = driver.page_source
    print(html)
    driver.close()


if __name__ == "__main__":
    chromeHeaderless()