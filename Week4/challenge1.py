# 기사제목 언론사 헤더 추가
import requests
from bs4 import BeautifulSoup

raw = requests.get("https://search.naver.com/search.naver?&where=news&query=%EC%BD%94%EC%95%8C%EB%9D%BC&sm=tab_tmr&frm=mr&nso=so:r,p:all,a:all&sort=0")

html = BeautifulSoup(raw.text,'html.parser')

f = open("challenge1.csv","w")
f.write('제목,언론사\n')

news_lists = html.select('ul.type01 dl')
for news_list in news_lists:
    title = news_list.select_one('a._sp_each_title').text.replace(',',"")
    agency = news_list.select_one('span._sp_each_source').text.replace(',',"")
    print("제목: ", title)
    print("언론사: ", agency)
    f.write(title + ',' + agency + '\n')
f.close()