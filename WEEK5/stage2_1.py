#평점이 8.5 이상인 영화만 출력하기

import requests
from bs4 import BeautifulSoup

raw=requests.get("https://movie.naver.com/movie/running/current.nhn",
                 headers={"User-Agent":"Mozilla/5.0"})
html=BeautifulSoup(raw.text,"html.parser")

#컨테이너 dl.lst_dsc
#제목 dt.tit a
#평점 dl.info_star div.star_t1 span.num
#장르 dl.info_txt1 dd a
#감독 dl.info_txt1 dd a
#배우 dl.info_txt1 dd a

movies=html.select("dl.lst_dsc")
for m in movies:
    title=m.select_one("dt.tit a").text.strip()
    score=m.select_one("dl.info_star div.star_t1 span.num").text
    genre=m.select("dl.info_txt1 dd:nth-of-type(1) a")
    director=m.select("dl.info_txt1 dd:nth-of-type(2) a")
    action=m.select("dl.info_txt1 dd:nth-of-type(3) a")

    if (float(score)<8.5):
        continue

    print(title)
    print(score)
    for g in genre:
        print(g.text.strip(),end="/")
    print("")
    for d in director:
        print(d.text.strip(), end="/")
    print("")
    for a in action:
        print(a.text.strip(), end="/")
    print("")
    print("="*50)
