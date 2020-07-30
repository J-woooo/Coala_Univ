# ycombinator 뉴스에서 순위, 제목을 출력하기
# 순위: tr.athing span.rank
# 제목: tr.athing a.storylink
import requests
from bs4 import BeautifulSoup

page = 1

for page in range(1):
    raw = requests.get("https://news.ycombinator.com/news?p="+str(page), headers = {'User-Agent':'Moziila/5.0'})
    html = BeautifulSoup(raw.text,'html.parser')

    articles = html.select('tr.athing')
    for article in articles:
        rank = article.select_one('span.rank').text
        title = article.select('a.storylink').text
        print("순위: ", rank)
        print("제목: ", title)
        print("=="*40)