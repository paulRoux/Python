from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, WebDriverException
from lxml import etree
from time import sleep

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 30)


def search():
	browser.get('https://www.jd.com/')
	try:
		input = wait.until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#key"))
		)  #llist
		submit = wait.until(
			EC.element_to_be_clickable((By.CSS_SELECTOR,"#search > div > div.form > button"))
		)
		# input = browser.find_element_by_id('key')
		input[0].send_keys('美食')
		submit.click()

		total = wait.until(
			EC.presence_of_all_elements_located(
				(By.CSS_SELECTOR,'#J_bottomPage > span.p-skip > em:nth-child(1) > b')
			)
		)
		html = browser.page_source
		praseHtml(html)
		return total[0].text
	except TimeoutException:
		search()


def nextPage(pageNumber):
	try:
		# 滑动到底部，加载出后三十个货物信息
		while len(browser.find_elements_by_class_name('gl-item')) < 60:
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			sleep(1)
        # 翻页动作
		button = wait.until(
			EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_bottomPage > span.p-num > a.pn-next > em'))
		)
		button.click()
		wait.until(
			EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#J_goodsList > ul > li:nth-child(60)"))
		)
	    # 判断翻页成功
		wait.until(
			EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#J_bottomPage > span.p-num > a.curr"), str(pageNumber))
		)
		html = browser.page_source
		praseHtml(html)
	except TimeoutException:
		nextPage(pageNumber)
	except WebDriverException:
		pass


def praseHtml(html):
	html = etree.HTML(html)
	items = html.xpath('//li[@class="gl-item"]')
	for item in items:
		# 此处的图片有的无法获取，目前已知原因是图片存在两个属性里面，但是进行多样的判断也是有相反部分无法获取
		img = item.xpath('.//div[@class="p-img"]//img/@data-lazy-img')
		if str(img) == "done":
			img = item.xpath('.//div[@class="p-img"]//img/@src')
		product = {
			'image': img,
			'title': item.xpath(".//div/a/em/text()"),
			'price': item.xpath(".//div/strong/i/text()"),
			'shop': item.xpath(".//div/span/a/@title"),
			'commit': item.xpath('.//div/strong/a/text()')
		}
		print(product)


def main():
	print("第", 1, "页：")
	total = int(search())
	for i in range(2, total+1):
		sleep(3)
		print("第", i, "页：")
		nextPage(i)


if __name__ == "__main__":
	main()
	browser.close()