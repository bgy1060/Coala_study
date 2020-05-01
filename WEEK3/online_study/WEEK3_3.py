import requests
from bs4 import BeautifulSoup

page=1
for page in range(1,11):

    raw=requests.get("https://www.caltech.edu/about/news?&p="+str(page),
                     headers={"User-Agent":"Mozilla/5.0"})
    html=BeautifulSoup(raw.text,"html.parser")

    #컨테이너 div.article-teaser
    #제목 div.article-teaser__title
    #날짜 div.article-teaser__published-date

    container=html.select("div.article-teaser")

    for cont in container:
        title=cont.select_one("div.article-teaser__title").text.strip()
        date=cont.select_one("div.article-teaser__published-date").text.strip()

        print(date,"/",title)
        print("="*50)