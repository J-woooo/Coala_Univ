# 네이버 tv에 원하는 검색어 입력 후 데이터 저장하기
import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    wb = openpyxl.load_workbook("review_homework1.xlsx")
    sheet = wb.active
    print("파일 불러오기 성공")
except:
    print("새로운 파일을 생성합니다.")
    wb = openpyxl.Workbook()     
    sheet = wb.active
    sheet.append(["검색어","제목","채널"])

keyword = input("검색어 입력: ")
page = 1
for page in range(1,4):
    raw = requests.get("https://tv.naver.com/search/clip?query="+keyword+"&sort=rel&page="+str(page)+"&isTag=false")
    html = BeautifulSoup(raw.text,'html.parser')
    # div.newsColl div.coll_cont 
    container = html.select("div.inner")
    # print(articles)
    for cont in container:
        title = cont.select_one("dt.title")
        chn = cont.select_one("span.ch_txt")
        # hit = cont.select_one("span.hit")
        # like = cont.select_one("span.like")

        print(title)
        print(chn)
        # print(hit.text.strip())
        # print(like.text.strip())
        print("="*50)
        # sheet.append([keyword,title,chn])
    
wb.save("review_homework1.xlsx")