from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.mvmnext.hu/")

id = driver.find_element_by_id("<div id="nemletezik"></div>")
q.send_keys("input")

submit = driver.find_element_by_name("submit")
submit.click()

driver.close()
