import requests
from bs4 import BeautifulSoup
import openpyxl
from urllib.request import urlretrieve

# keyword = input("검색어를 입력해주세요 >> ")
# maxPrice = input("적정 가격을 입력해주세요 >> ")

keyword = "송강호"
maxPrice = 15000
maxPrice = int(maxPrice)
page = 1

raw = requests.get("https://watcha.com/ko-KR/search?query="+str(keyword),
                    headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text,'html.parser')

# div.css-chidac-ScrollBar.e1f5xhlb1 li.css-106b4k6-Self.e3fgkal0
# li.css-106b4k6-Self.e3fgkal0
movieList = html.select("li.css-106b4k6-Self.e3fgkal0")
# 영화, 제목, 연도, 나라

for movie in movieList:
    title = movie.select_one("div.css-gt67eo-TopResultItemTitle.e1m1t8xe1").text
    url = movie.attrs["href"]

    year_country = movie.select_one("div.css-aeixur-TopResultItemExtraInfo,e1m1t8xe2").text
    year = year_country[0:4]
    country = year_country[7:]
    print(title)
    print(year)        
    print(country)

    raw_each = requests.get(url, headers = {"User-Agent":"Mozilla/5.0"})
    html_each = BeautifulSoup(raw_each.text,'html.parser')

    # actor_list = html_each.select_one("div.css-150y45-ScrollingInner.e1f5xhlb2 li.css-1od386f-Self.e1hyxz9l0")
    # for()

