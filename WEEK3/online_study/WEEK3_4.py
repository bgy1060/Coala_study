import requests
from bs4 import BeautifulSoup

page=1
for page in range(1,100,50):

    raw=requests.get("https://www.melon.com/new/index.htm#params%5BareaFlg%5D=I&po=pageObj&startIndex="+str(page),
                     headers={"User-Agent":"Mozilla/5.0"})
    html=BeautifulSoup(raw.text,"html.parser")

    #컨테이너 table tbody tr
    #제목 div.ellipsis.rank01
    #가수 div.ellipsis.rank02

    container=html.select("table tbody tr")

    for cont in container:
        title=cont.select_one("div.ellipsis.rank01").text.strip()
        singer=cont.select_one("div.ellipsis.rank02").text.strip()

        print(title,"/",singer)
        print("="*50)