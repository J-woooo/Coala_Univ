# 다음 영화 페이지에서 각 영화에 제목, 평점, 장르, 감독, 배우 데이터를 수집하기
# 빠른 예매에 들어가서 예매 순위에 영화 리스트 데이터에서 상세 페이지 안에서 데이터 수집하기
# 다음 영화는 전체 url이 다 들어있으므로 그대로 접속하면 된다.
# 데이터 수집을 마치고 데이터를 파일로 저장하기

import requests
from bs4 import BeautifulSoup
import openpyxl
from urllib.request import urlretrieve

raw = requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx",
                    headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text,'html.parser')

movies = html.select("ul.list_boxthumb > li")

for movie in movies:
    title = movie.select_one("strong.tit_join > a")
    url = title.attrs["href"]

    raw_each = requests.get(url, headers = {"User-Agent":"Mozilla/5.0"})
    html_each = BeautifulSoup(raw_each.text,'html.parser')

    
    each_title = html_each.select_one("strong.tit_movie").text
    score = html_each.select_one("em.emph_grade").text

    genre = html_each.select_one("dl.list_movie > dd:nth-of-type(1)").text
    director = html_each.select("dl.list_movie > dd:nth-of-type(5) a")
    actor = html_each.select("dl.list_movie > dd:nth-of-type(6) a")

    print("제목: ",each_title)
    print("평점: ",score)
    print("장르: ",genre)   
    print("감독: ")
    for d in director:
        print(d.text)
    print("배우: ")
    for a in actor:
        print(a.text)
    print("="*50)