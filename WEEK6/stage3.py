from selenium import webdriver
import time

driver=webdriver.Chrome("C:/chromedriver")

driver.get("https://v4.map.naver.com/")

search_box=driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("치킨")

search_button=driver.find_element_by_css_selector("button.spm")
search_button.send_keys('\n')

for n in range(1,5):
    time.sleep(1)

    stores=driver.find_elements_by_css_selector("div.lsnx")

    for s in stores:
        name=s.find_element_by_css_selector("dt>a").text
        addr=s.find_element_by_css_selector("dd.addr").text
        phone=s.find_element_by_css_selector("dd.tel").text

        print(name,addr,phone)
        print("="*50)

    page_bar=driver.find_elements_by_css_selector("div.paginate > *")
    page_bar[n+1].send_keys('\n')
    time.sleep(1)

driver.close()