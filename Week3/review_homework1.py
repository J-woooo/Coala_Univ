# Bing에서 코알라를 검색하고 나오는 뉴스 타이틀과 요약기사를 수집하기
import requests
from bs4 import BeautifulSoup

for page in range(1,8,3):
    raw = requests.get("https://www.bing.com/news/search?q=%EC%BD%94%EC%95%8C%EB%9D%BC&qs=n&form=QBNT&sp=-1&pq=%EC%BD%94%EC%95%8C%EB%9D%BC&sc=8-3&sk=&cvid=B6AFF8D626B44942BEB23110B8D6DE72"+str(page))
    html = BeautifulSoup(raw.text,'html.parser')

    articles = html.select('div.news-card-body div.t_s')
    for article in articles:
        title = article.select_one('div.t_t').text
        summary = article.select_one('div.snippet').text
        print("제목: ", title)
        print("요약: ", summary)
        print("=="*40)