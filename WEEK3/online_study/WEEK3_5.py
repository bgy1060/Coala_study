import requests
from bs4 import BeautifulSoup

for index in range(1,200,50):
    raw = requests.get("https://www.melon.com/search/song/index.htm?q=%EC%82%AC%EB%9E%91&section=&searchGnbYn=Y&kkoSpl=N&kkoDpType=&ipath=srch_form#params%5Bq%5D=%25EC%2582%25AC%25EB%259E%2591&params%5Bsort%5D=hit&params%5Bsection%5D=all&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex="
    +str(index),headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text, "html.parser")

    container = html.select("div.tb_list tbody tr")
    for cont in container:
        title = cont.select_one("div.tb_list tbody tr a.fc_gray").text
        artist = cont.select_one("div.tb_list tbody tr div#artistName span.checkEllipsisSongdefaultList").text

        print(artist,"-",title)