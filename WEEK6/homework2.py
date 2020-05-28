from selenium import webdriver
import time

# 웹 드라이버 열기
driver = webdriver.Chrome("./chromedriver")

# url 입력
driver.get("https://www.instagram.com/")
time.sleep(2)

# 아이디 입력창 선택, 아이디 입력
## 아이디, 비밀번호 입력창 선택자가 동일, idpw_box에 리스트로 저장
idpw_box = driver.find_elements_by_css_selector("label.f0n8F input")
idpw_box[0].send_keys("id")

# 비밀번호 입력
idpw_box[1].send_keys("password")

# 로그인 버튼 선택, 클릭
login_button = driver.find_element_by_css_selector("button.sqdOP.L3NKy.y3zKF")
login_button.click()
time.sleep(3)

# 팝업 닫기버튼 선택, 클릭
close_button = driver.find_element_by_css_selector("div.mt3GC button.aOOlW.HoLwm")
close_button.click()

# 검색창 선택, 클릭하여 활성화
search_box = driver.find_element_by_css_selector("div.pbgfb.Di7vw")
search_box.click()

# 검색어 입력 박스 선택, 검색어 입력
input_box = driver.find_element_by_css_selector("div.LWmhU._0aCwM input")
input_box.send_keys("ootd")
time.sleep(3)

# 검색결과 리스트 중 검색어 결과('#ootd') 선택
# 리스트 선택
search_lists = driver.find_elements_by_css_selector("a.yCE8d")

# 리스트의 각 요소 중 제목과 검색어가 같은 경우 찾기
for x in search_lists:
    if x.find_element_by_css_selector("span.Ap253").text == "#ootd":
        # 해당 요소의 하이퍼링크 저장
        new_link = x.get_attribute("href")
        break

# 선택한 결과의 하이퍼링크 페이지로 이동
driver.get(new_link)
time.sleep(4)

# 검색 결과 페이지에서 12개의 게시물 리스트 선택
contents = driver.find_elements_by_css_selector('div.v1Nh3.kIKUG._bz0w a')[:12]
content_num = 1

# 각 게시물 별로 본문 내용 수집
for content in contents:
    # 12-1 게시물 클릭
    content.click()
    time.sleep(4)

    # 본문 선택, 출력
    text = driver.find_element_by_css_selector('div.C4VMK > span').text
    print(str(content_num)+"번째 게시글\n"+text+"\n======================================")

    # 닫기 버튼 선택, 클릭
    content_close = driver.find_element_by_css_selector('div.Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG button')
    content_close.click()
    content_num += 1
    time.sleep(1)

driver.close()


