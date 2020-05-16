import requests
from bs4 import BeautifulSoup
f=open("navertv.csv",'w',encoding='UTF-16')
f.write('제목,채널명,재널명,재생수,좋아요\n')

row=requests.get("https://tv.naver.com/r")
html=BeautifulSoup(row.text, "html.parser")

#컨테이너 div.cds_type
#제목 dt.title
#채널명 dd.chn
#재생수 span.hit
#좋아요 span.like


clips=html.select('div.cds_type')

for rank in range(97):
    title = clips[rank].select_one('dt.title').text.strip() # 하나만 찾을때는 select_one을 쓴다.
    # select한 결과물은 코드 형식이다. 이 뒤에 text를 붙여주면 결과만 뽑아온다.
    chn = clips[rank].select_one('dd.chn').text.strip()
    hit = clips[rank].select_one('span.hit').text.strip()
    like = clips[rank].select_one('span.like').text.strip() #strip()를 이용해서 공백 제거

    title=title.replace(",","")
    chn = chn.replace(",","")
    hit = hit.replace(",","")
    like =like.replace(",","")
    #print(title,chn,hit,like)

    hit = hit.replace("재생 수", "")
    like = like.replace("좋아요 수", "")

    f.write(title+","+chn+","+hit+","+like+"\n")

f.close()