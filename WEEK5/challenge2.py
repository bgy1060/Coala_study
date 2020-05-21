#IMDb 포스터 저장하기

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from multiprocessing import Pool

raw=requests.get("https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd",
                 headers={"User-Agent":"Mozilla/5.0"})
html=BeautifulSoup(raw.text,"html.parser")

#컨테이너 div.lister-item
#제목 h3.lister-item-header a
#평점 div.ipl-rating-star.small span.ipl-rating-star__rating
#감독&배우 p.text-muted.text-small a

movies=html.select("div.lister-item")

for m in movies:
    title=m.select_one("h3.lister-item-header a")
    score=m.select_one("div.ipl-rating-star.small span.ipl-rating-star__rating")
    director_action=m.select("div.lister-item p:nth-of-type(3) a")

    print("<영화제목>")
    print("- "+title.text.strip()+"\n")

    print("<평점>")
    if score is not None:
        print("- "+score.text.strip()+"\n")
    else:
        print("- 평점이 없습니다.\n")

    print("<영화 감독 & 배우>")
    for da in director_action:
        print("- "+da.text.strip())

    print("=" * 50)

    url="https://www.imdb.com/"+title.attrs["href"]

    raw_each = requests.get(url, headers={"User-Agnet": "Mozilla/5.0"})
    html_each = BeautifulSoup(raw_each.text, "html.parser")
    poster = html_each.select_one("div.poster img")
    poster_src = poster.attrs["src"]
    urlretrieve(poster_src, "IMDb_poster/" + title.text[:2] + ".png")

    #포스터 div.poster img


