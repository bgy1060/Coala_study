# Y-combinator news 데이터 수집하기

import requests
from bs4 import BeautifulSoup

page=1
for page in range(1,100):

    raw=requests.get("https://news.ycombinator.com/news?p="+str(page),
                     headers={'User-Agent':'Mozilla/5.0'})
    html=BeautifulSoup(raw.text,"html.parser")

    #컨테이너 tr.athing
    #랭킹 span.rank
    #이름 a.storylink

    container=html.select("tr.athing")
    for cont in container:
        rank=cont.select_one("span.rank").text.strip()
        name=cont.select_one("a.storylink").text.strip()
        print(rank,name)