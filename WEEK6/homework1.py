from selenium import webdriver

driver=webdriver.Chrome("C:/chromedriver.exe")

driver.get("https://nid.naver.com")

id=driver.find_element_by_css_selector("input#id")
id.send_keys("id")

pw=driver.find_element_by_css_selector("input#pw")
pw.send_keys("password")

login=driver.find_element_by_css_selector("input.btn_global")
login.click()

driver.close()