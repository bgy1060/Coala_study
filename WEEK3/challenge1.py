#1위부터 100위까지 NaverTV 데이터 수집하기

import requests
from bs4 import BeautifulSoup

raw=requests.get("https://tv.naver.com/r/")
html=BeautifulSoup(raw.text,"html.parser")

#1위부터 3위 정보 출력
container1=html.select("div.inner")
for cont1 in container1:
    title=cont1.select_one("dt.title").text.strip()
    chn=cont1.select_one("dd.chn").text.strip()
    hit=cont1.select_one("span.hit").text.strip()
    like=cont1.select_one("span.like").text.strip()
    print(title)
    print(chn)
    print(hit)
    print(like)
    print("="*50)

#4위부터 100위 정보 출력
container2=html.select("div.cds")
for cont2 in container2:
    title = cont2.select_one("dt.title").text.strip()
    chn = cont2.select_one("dd.chn").text.strip()
    hit = cont2.select_one("span.hit").text.strip()
    like = cont2.select_one("span.like").text.strip()
    print(title)
    print(chn)
    print(hit)
    print(like)
    print("=" * 50)
