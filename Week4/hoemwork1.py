# 네이버 시리즈 e북 TOP100 데이터 수집결과 저장하기(제목, 저자)
import requests
from bs4 import BeautifulSoup
import openpyxl

try:
    wb = openpyxl.load_workbook("homework1.xlsx")
    sheet = wb.active
    print("파일 불러오기 성공")
except:
    print("새로운 파일을 생성합니다.")
    wb = openpyxl.Workbook()     
    sheet = wb.active
    sheet.append(["순위","제목","저자"])
    
page = 1
for page in range(1,6):
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(page),headers = {'User-Agent':'Moziila/5.0'})
    html = BeautifulSoup(raw.text,'html.parser')
    book_lists = html.select('ul.lst_thum.v1')

    for book_list in book_lists:
        books = book_list.select('li')
        for book in books:
            rank =  book.select_one('span.num').text
            title = book.select_one('a strong').text
            author = book.select_one('a span.writer').text
            print("순위: ",rank)
            print("제목: ",title)
            print("저자: ",author)
            print("=="*40)
            sheet.append([rank,title,author])
    
wb.save("homework1.xlsx")