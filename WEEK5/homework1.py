#다음 영화 데이터 수집하기

import requests
from bs4 import BeautifulSoup

raw=requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx"
                 ,headers={"User-Agent":"Mozilla/5.0"})
html=BeautifulSoup(raw.text,"html.parser")

title=html.select_one("strong.tit_join>a")
url=title.attrs["href"]

raw_each=requests.get(url ,headers={"User-Agent":"Mozilla/5.0"})
html_each=BeautifulSoup(raw_each.text,"html.parser")

#컨테이너 div.movie_summary
#제목 div.subject_movie>strong.tit_movie
#평점 div.subject_movie a em.emph_grade
#장르 dl.list_movie.list_main dd:nth-of-type(1)
#배우 dd.type_ellipsis a
#감독 dd.type_ellipsis a

movies=html_each.select("div.movie_summary")
title=html_each.select_one("div.movie_summary").text.strip()
score=html_each.select_one("div.subject_movie a em.emph_grade").text.strip()
genre=html_each.select("dl.list_movie.list_main dd:nth-of-type(1)")
info=html_each.select("dd.type_ellipsis")
actor=info[0].select_one("a").text.strip()
#director=info[1].select_one("a").strip

print("<" + title.text.strip() + ">\n")
