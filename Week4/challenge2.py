# 엑셀 파일에 검색어 추가. 검색어, 기사제목, 언론사
import requests
from bs4 import BeautifulSoup
import openpyxl

keyword = input("검색어를 입력해주세요: ")

try:
    wb = openpyxl.load_workbook("challenge2.xlsx")
    sheet = wb.active
    print("파일 불러오기 성공")
except:
    print("새로운 파일을 생성합니다.")
    wb = openpyxl.Workbook()     
    sheet = wb.active
    sheet.append(["검색어","제목","언론사"])

raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+keyword)

html = BeautifulSoup(raw.text,'html.parser')

news_lists = html.select('ul.type01 dl')
for news_list in news_lists:
    title = news_list.select_one('a._sp_each_title').text.replace(',',"")
    agency = news_list.select_one('span._sp_each_source').text.replace(',',"")
    print("제목: ", title)
    print("언론사: ", agency)
    sheet.append([keyword,title,agency])
    
wb.save("challenge2.xlsx")