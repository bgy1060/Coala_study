import requests
from bs4 import BeautifulSoup
import openpyxl

keyword=input("검색어를 입력해주세요: ")
try:
    wb=openpyxl.load_workbook("navernews.xlsx")
    sheet = wb.active
except:
    wb=openpyxl.Workbook()
    sheet=wb.active
    sheet.append(["제목","언론사"])

for page in range(1,100,10):

    url='https://search.naver.com/search.naver?&where=news&query='+keyword+'&start='+str(page)
    row=requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    html=BeautifulSoup(row.text, "html.parser")

    #컨테이너 ul.type01>li
    #기사 제목 a._sp_each_title
    #신문사 span._sp_each_source

    articles= html.select('ul.type01>li')

    for news in articles:
        title=news.select_one('a._sp_each_title').text.strip()
        journal = news.select_one('span._sp_each_source').text.strip()
        print(title,journal)
        sheet.append([title,journal])

wb.save("navernews.xlsx")