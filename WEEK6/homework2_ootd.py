from selenium import webdriver
import time

# 웹 드라이버 열기
driver=webdriver.Chrome("C:/chromedriver.exe")

# url 입력
driver.get("https://www.instagram.com/explore/tags/ootd/")

# 로그인 버튼 링크 속성 값 가져오기
login=driver.find_elements_by_css_selector("a.tdiEy")
login_url=login[0].get_attribute("href")

# 로그인 버튼 링크로 이동
driver.get(login_url)

time.sleep(3)

# login input 요소 저장
login_box=driver.find_elements_by_css_selector("label.f0n8F input")

# 아이디 입력
id=login_box[0]
id.send_keys("id")

# 비밀번호 입력
password=login_box[1]
password.send_keys("password")

# 로그인 버튼 클릭
login_button=driver.find_elements_by_css_selector("button.sqdOP")
login_button[1].click()
time.sleep(3)

# 12개 포스트 출력
for i in range(12):

    # 포스트 컨테이너 수집
    post=driver.find_elements_by_css_selector("div.v1Nh3")

    # (i+1)번째 포스트 클릭
    post[i].click()
    time.sleep(1)

    print("<" + str(i + 1) + "번째 게시물>\n")

    # 포스트 내용이 없는 경우 예외처리
    try:
        # 포스트 내용 가져온 후 출력
        post_text=driver.find_element_by_css_selector("div.C4VMK span").text
        print(post_text)

    except:
        # 포스트 내용이 없다면 포스트 내용이 없다고 출력
        print("포스트 내용이 없습니다.")

    print("="*50)

    time.sleep(1)
    
    # 포스트 닫기 버튼 클릭
    close_button=driver.find_element_by_css_selector("div.Igw0E button.wpO6b ")
    close_button.click()
    time.sleep(1)

# driver 종료
driver.close()

