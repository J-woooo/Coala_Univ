# 다음 뉴스 검색결과에서 제목, 요약부분 엑셀로 저장
import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    wb = openpyxl.load_workbook("homework2.xlsx")
    sheet = wb.active
    print("파일 불러오기 성공")
except:
    print("새로운 파일을 생성합니다.")
    wb = openpyxl.Workbook()     
    sheet = wb.active
    sheet.append(["제목","요약"])

page = 1
for page in range(1,4):
    raw = requests.get("https://search.daum.net/search?w=news&q=%EC%BD%94%EC%95%8C%EB%9D%BC&DA=PGD&spacing=0&p="+str(page))
    html = BeautifulSoup(raw.text,'html.parser')
    # div.newsColl div.coll_cont 
    articles = html.select('div#newsColl.type_fulltext.wid_n div.coll_cont li')
    # print(articles)
    for article in articles:
        title = article.select_one('div.wrap_tit.mg_tit').text
        summary = article.select_one('p.f_eb.desc').text
        print("제목: ",title)
        print("요약: ",summary)
        print("=="*50)
        sheet.append([title,summary])
    
wb.save("homework2.xlsx")