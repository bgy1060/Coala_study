import requests
from bs4 import BeautifulSoup

page=1
for page in range(21):

    raw=requests.get("http://www.jobkorea.co.kr/Starter/?&Page="+str(page),
                     headers={"User-Agent":"Mozilla/5.0"})
    html=BeautifulSoup(raw.text,"html.parser")


    #컨테이너 ul.filterList li
    #회사이름 div.coTit a
    #채용 정보 div.tit a
    #세부 채용 정보 div.sTit span

    job=html.select("ul.filterList li")
    for j in job:
        company=j.select_one("div.coTit a")
        job_info=j.select_one("div.tit a")
        job_sub_info=j.select("div.sTit span")

        print("- 회사 :"+company.text.strip())
        print("- 채용 정보 :"+job_info.text.strip())
        print("- 세부 채용 정보 :",end="")
        for jsi in job_sub_info:
            print(jsi.text.strip(), end="/")
        print("")
        print("="*50)
