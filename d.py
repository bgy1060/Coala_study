from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("https://papago.naver.com/")
sent = input("번역할 내용 입력 : ")
lan = int(input("1. 영어 2. 일본어 3. 중국어 : "))

driver.find_element_by_css_selector("textarea#txtSource").send_keys(sent)
driver.find_elements_by_css_selector("span.btn_dropdown_arr___2xcBb")[1].click()
time.sleep(0.5)
year_select = driver.find_elements_by_css_selector("ul.dropdown_menu_inner___29_zc")[1]
for option in year_select.find_elements_by_tag_name('span'):
    if lan == 1:
        if option.text == "영어":
            option.click()
            break
    elif lan == 2:
        if option.text == "일본어":
            option.click()
            break
    elif lan == 3:
        if option.text == "중국어(간체)":
            option.click()
            break
    else:
        print("잘못입력")
