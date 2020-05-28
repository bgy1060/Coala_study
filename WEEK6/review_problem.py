from selenium import webdriver

driver=webdriver.Chrome("C:/chromedriver.exe")

driver.get("https://finance.naver.com/sise/sise_group.nhn?type=upjong")
name=driver.find_elements_by_css_selector("tr>td>a")
fluctuation=driver.find_elements_by_css_selector("span.tah")

print("< 국내증시 업종별 시세 정보 >")
print("="*50)

for i in range(len(name)-5):
    print("##### 업종명 #####")
    print(name[i].text+"\n")
    print("##### 전일대비 #####")
    print(fluctuation[i].text)
    print("="*50)

driver.close()