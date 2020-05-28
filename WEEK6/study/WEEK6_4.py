from selenium import webdriver
import time

driver=webdriver.Chrome("C:/chromedriver.exe")

driver.get("https://v4.map.naver.com/")

#팝업창 닫기
close_box=driver.find_element_by_css_selector("div.popup_content button.btn_close")
close_box.click()

find_load=driver.find_elements_by_css_selector("li a.spm")
find_load[1].send_keys("\n")

time.sleep(1)

input=driver.find_elements_by_css_selector("input.input_act")

#출발지
input[1].send_keys("이화여자대학교")
input[1].send_keys("\n")
time.sleep(2)

#도착지
input[2].send_keys("청계천")
input[2].send_keys("\n")
time.sleep(2)

start=driver.find_elements_by_css_selector("div.pf_act a.spm")
start[2].click()
time.sleep(2)

path=driver.find_elements_by_css_selector("div.path_num span.spm")
for i in range(len(path)):
    print("<"+path[i].text+">\n")

    detail_path=driver.find_elements_by_css_selector("div.fw_path_traffic")
    for j in range(len(detail_path)):
        print(detail_path[j].text)

    print("="*50)