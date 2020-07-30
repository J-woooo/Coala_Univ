import requests
from bs4 import BeautifulSoup

data = requests.get("https://tv.naver.com/r/")
html = BeautifulSoup(data.text,'html.parser')
print(html)
# 제목: dt.title
# 채널명: dd.chn
# 재생수: span.hit
# 좋아요수: span.like

container = html.select("div.cds")

for cont in container:
    title = cont.select_one("dt.title")
    chn = cont.select_one("dd.chn")
    hit = cont.select_one("span.hit")
    like = cont.select_one("span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50)