# 네이버 e북 데이터 수집하기

import requests
from bs4 import BeautifulSoup

page=1
for page in range(1,6):
    raw=requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(page),
                     headers={"User-Agent":"Mozilla/5.0"})
    html=BeautifulSoup(raw.text,"html.parser")

    #컨테이너 div.lst_thum_wrap li
    #제목 div.lst_thum_wrap li>a strong
    #저자 span.writer

    container=html.select("div.lst_thum_wrap li")

    for cont in container:
        name=cont.select_one("div.lst_thum_wrap li>a strong").text.strip()
        writer=cont.select_one("span.writer").text.strip()
        print(name+"-"+writer)