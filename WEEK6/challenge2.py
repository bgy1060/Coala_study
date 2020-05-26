from selenium import webdriver
import time

driver=webdriver.Chrome("C:/chromedriver.exe")

driver.get("https://www.google.com/maps/")

search_box=driver.find_element_by_css_selector("div#gs_lc50 input:nth-of-type(1)")
search_box.send_keys("카페")

search_button=driver.find_element_by_css_selector("div.searchbox-searchbutton-container button.searchbox-searchbutton")
search_button.click()

for i in range(100):

    time.sleep(5)

    cafe=driver.find_elements_by_css_selector("div.section-result-content")
    for c in cafe:
        name=c.find_element_by_css_selector("h3.section-result-title").text
        try:
            rank=c.find_element_by_css_selector("span.cards-rating-score").text
        except:
            rank=""
        addr=c.find_element_by_css_selector("span.section-result-location").text

        print("카페 이름: "+name)
        print("카페 주소: "+addr)
        print("카페 점수: "+rank)
        print("="*50)

    try:
        next_button=driver.find_element_by_css_selector("button.n7lv7yjyC35__button:nth-of-type(2)")
        next_button.click()
    except:
        print("우리 동네 카페 수는 "+str(i)+"개!")
        print("데이터 수집 끝!")
        break

driver.close()