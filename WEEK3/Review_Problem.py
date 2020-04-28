# Naver Music 1위부터 100위까지 노래 정보를 수집하기

import requests
from bs4 import BeautifulSoup

page=1

for page in range(1,3):
    raw=requests.get("https://music.naver.com/chart/musicianLeague.nhn?duration=DAILY&page="+str(page),
                     headers={"User-Agent":"Mozilla/5.0"})
    html=BeautifulSoup(raw.text,"html.parser")

    #컨테이너 tbody tr
    #순위 span.num
    #곡명 td.tb_name > span.tit
    #아티스트 td.tb_artist > span.tit
    container= html.select("tbody tr")

    for cont in container:
        num=cont.select_one("span.num").text.strip()
        name=cont.select_one("td.tb_name > span.tit").text.strip()
        artist=cont.select_one("td.tb_artist > span.tit").text.strip()
        print(num,name,artist)
        print("="*50)