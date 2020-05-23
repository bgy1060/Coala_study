#challenge1 파파고 영단어 해석기 만들기

from selenium import webdriver
import time
driver=webdriver.Chrome("./chromedriver")

driver.get("https://papago.naver.com/")

time.sleep(0.5)
#검색창 textarea#txtSource
input_box=driver.find_element_by_css_selector("textarea#txtSource")
input_box.send_keys("seize the day")

search_button=driver.find_element_by_css_selector("button#btnTranslate")
search_button.click()

time.sleep(0.5)
result=driver.find_element_by_css_selector("div#txtTarget").text
print(result)
