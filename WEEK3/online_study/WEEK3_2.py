import requests
from bs4 import BeautifulSoup

day=["mon","tue","wed","thu","fri","sat","sun"]
page=0
for d in day:
    raw=requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week="+d,
                     headers={"User-Agent":"Mozilla/5.0"})
    html=BeautifulSoup(raw.text,"html.parser")

    #컨테이너 ul.img_list li
    #제목 ul.img_list li dt
    #작가 ul.img_list li dd.desc
    container=html.select("ul.img_list li")

    for cont in container:
        title=cont.select_one("ul.img_list li dt").text.strip()
        writer=cont.select_one("ul.img_list li dd.desc").text.strip()
        print(title,writer)
        print("="*50)

