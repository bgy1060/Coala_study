# 다음뉴스 기사 데이터 수집하기

import requests
from bs4 import BeautifulSoup

page=1

for page in (1,3):

    raw=requests.get("https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EC%BD%94%EC%95%8C%EB%9D%BC&p="+str(page))
    html=BeautifulSoup(raw.text,"html.parser")

    #컨테이너 ul#clusterResultUL > li
    #기사 제목 a.f_link_b
    #기사 요약 div.cont_inner p

    container=html.select("ul#clusterResultUL > li")

    for cont in container:
        name=cont.select_one("a.f_link_b").text.strip()
        summary = cont.select_one("div.cont_inner p").text.strip()
        print(name)
        print(summary)
        print("="*50)