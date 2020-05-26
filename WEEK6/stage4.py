from selenium import webdriver
import time

driver=webdriver.Chrome("C:/chromedriver.exe")

driver.get("https://v4.map.naver.com/")

#팝업창 닫기
close_box=driver.find_element_by_css_selector("div.popup_content button.btn_close")
close_box.click()

#검색어 입력
search_box=driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("치킨")

#검색 버튼 클릭
search_button=driver.find_element_by_css_selector("button.spm")
search_button.send_keys("\n")

#컨테이너 div.lsnx
#가게 이름 dl>dt>a
#주소 dd.addr
#전화번호 dd.tel

for p in range(1,100):

    time.sleep(1)

    store=driver.find_elements_by_css_selector("div.lsnx")

    for s in store:
        name=s.find_element_by_css_selector("dl>dt>a").text
        addr=s.find_element_by_css_selector("dd.addr").text.replace("지번","")
        try:
            tel = s.find_element_by_css_selector("dd.tel").text
            print(name + "/" + addr + "/" + tel)
        except:
            print(name + "/" + addr )

        print("="*50)

    page=driver.find_elements_by_css_selector("div.paginate >*")
    try:
        if p % 5 != 0:
            page[p % 5 + 1].send_keys("\n")
        else:
            page[6].send_keys("\n")
    except:
        print("우리 동네 치킨집은 "+p+"개!")
        print("데이터 수집 완료!")
        break
driver.close()
