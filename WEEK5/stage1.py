import requests
from bs4 import BeautifulSoup

raw=requests.get("https://movie.naver.com/movie/running/current.nhn"
                , headers={'User-Agent':'Mozilla/5.0'})
html=BeautifulSoup(raw.text,'html.parser')

#컨테이너 ul.lst_detail_t1 li
#영화제목 dt.tit a
#평점 dd a span.num
#장르
#감독
#배우

movies=html.select("ul.lst_detail_t1 li")
for movie in movies:
    title=movie.select_one("dt.tit a").text.strip()
    star=movie.select_one("div.star_t1 span.num").text.strip()
    genre=movie.select_one("dl.info_txt1 dd a ").text.strip()
    #print(title)
    #print(star)

    #infos=movie.select('dl.info_txt1 dd')
    #print(infos[0].select_one('a').text.strip())
    #print(infos[1].select_one('a').text.strip())
    #print(infos[2].select_one('a').text.strip())

    infos1=movie.select('dl.info_txt1 dd:nth-of-type(1) a')
    infos2 = movie.select('dl.info_txt1 dd:nth-of-type(2) a')
    infos3 = movie.select('dl.info_txt1 dd:nth-of-type(3) a')

    for g in infos1:
        print(g.text)
    for g in infos2:
        print(g.text)
    for g in infos3:
        print(g.text)
    print('-'*20)

