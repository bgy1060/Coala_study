#네이버 영화에서 데이터 수집하기_리스트 활용

import requests
from bs4 import BeautifulSoup

raw=requests.get("https://movie.naver.com/movie/running/current.nhn",
                 headers={"User-Agent":"Mozilla/5.0"})

html= BeautifulSoup(raw.text,"html.parser")

#컨테이너 dl.lst_dsc
#제목 dt.tit a
#평점 dl.info_star div.star_t1 span.num
#장르 dl.info_txt1 dd a
#감독 dl.info_txt1 dd a
#배우 dl.info_txt1 dd a

movies=html.select("dl.lst_dsc")
for m in movies:
    title=m.select_one("dt.tit a").text.strip()
    score=m.select_one("dl.info_star div.star_t1 span.num").text.strip()
    info=m.select("dl.info_txt1 dd")
    genre=info[0].select("a")
    director=info[1].select("a")
    action=info[2].select("a")

    print(title)
    print(score)
    for g in genre:
        print(g.text.strip(),end="/")
    print("")
    for d in director:
        print(d.text.strip(),end="/")
    print("")
    for a in action:
        print(a.text.strip(), end="/")
    print("")
    print("="*50)