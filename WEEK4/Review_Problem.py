import requests
from bs4 import BeautifulSoup

import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

sheet.append(["순위", "제목","아티스트"])
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

        sheet.append([num, name,artist])

wb.save("navermusic.xlsx")