#IMDb 영화정보 수집하기

import requests
from bs4 import BeautifulSoup

raw=requests.get("https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd",
                 headers={"User-Agent":"Mozilla/5.0"})
html=BeautifulSoup(raw.text,"html.parser")

#컨테이너 div.lister-item
#제목 h3.lister-item-header a
#평점 div.ipl-rating-star.small span.ipl-rating-star__rating
#감독&배우 p.text-muted.text-small a

movies=html.select("div.lister-item")

for m in movies:
    title=m.select_one("h3.lister-item-header a").text.strip()
    score=m.select_one("div.ipl-rating-star.small span.ipl-rating-star__rating")
    director_action=m.select("div.lister-item p:nth-of-type(3) a")

    print("<영화제목>")
    print("-"+title+"\n")

    print("<평점>")
    if score is not None:
        print("- "+score.text.strip()+"\n")
    else:
        print("- 평점이 없습니다.\n")

    print("<영화 감독 & 배우>")
    for da in director_action:
        print("- "+da.text.strip())

    print("=" * 50)






