#웹 상의 이미지 데이터 저장하기

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

raw=requests.get("https://movie.naver.com/movie/running/current.nhn",
                 headers={"User-Agent":"Mozilla/5.0"})
html=BeautifulSoup(raw.text,"html.parser")

movies=html.select("dl.lst_dsc")

for m in movies:
    title=m.select_one("dt.tit a")
    print("<"+title.text.strip()+">\n")

    url="https://movie.naver.com"+title.attrs["href"]

    raw_each=requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
    html_each=BeautifulSoup(raw_each.text,"html.parser")

    #컨테이너 div.score_result li
    #평점 div.score_result div.star_score em
    #리뷰 div.score_result div.score_reple p

    container=html_each.select("div.score_result li")
    poster = html_each.select_one("div.mv_info_area div.poster img")
    poster_src = poster.attrs["src"]

    urlretrieve(poster_src, "poster/" + title.text[:2] + ".png")
    for cont in container:
        score=cont.select_one("div.score_result div.star_score em").text.strip()
        review=cont.select_one("div.score_result div.score_reple p").text.strip()
        print(score+"점 "+review)
    print("="*50)
