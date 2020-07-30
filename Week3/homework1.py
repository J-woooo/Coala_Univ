# 네이버 시리즈 e-book top100 수집하기 1~100위 제목 저자 출력창에 출력
import requests
from bs4 import BeautifulSoup

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