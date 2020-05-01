import requests
from bs4 import BeautifulSoup

page=0
for page in range(0,41,10):

    raw=requests.get("http://www.ewha.ac.kr/ewha/news/movie.do?mode=list&&articleLimit=10&article.offset="+str(page),
                     headers={"User-Agent":"Mozilla/5.0"})
    html=BeautifulSoup(raw.text,"html.parser")

    #컨테이너 div.b-box02
    #제목 div.b-title-box
    #요약 div.b-text-box
    #날짜 li.b-date
    #조회수 li.b-hit

    container=html.select("div.b-box02")

    for cont in container:
        title=cont.select_one("div.b-title-box").text.strip()
        summary=cont.select_one("div.b-text-box").text.strip()
        date=cont.select_one("li.b-date").text.strip()
        hit=cont.select_one("li.b-hit").text.strip()
        print(title)
        print(summary)
        print(date,hit)
        print("="*50)