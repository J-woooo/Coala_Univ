# 쿠팡 크롤러

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

keyword = input("검색어를 입력해주세요 >> ")
maxPrice = input("적정 가격을 입력해주세요 >> ")


maxPrice = int(maxPrice)
page = 1

raw = requests.get("https://www.coupang.com/np/search?q="+str(keyword)+"&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page="+str(page)+"&rocketAll=false&searchIndexingToken=1=4&backgroundColor=",
                    headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text,'html.parser')

productList = html.select("ul.search-product-list li.search-product")

# dl.search-product-wrap dt.image img.search-product-wrap-img

print("==조건에 맞는 상품과 가격을 출력합니다==")
for page in range(1,2):
    for product in productList:
        title = product.select_one("div.name").text
        price = product.select_one("div.price-area strong.price-value").text
        price = int(price.replace(",",""))
        image = product.select_one("dt.image img.search-product-wrap-img")
        image_src = image.attrs["src"]
        image_src = "https:"+image_src
        if(price <= maxPrice):
            print(title)
            print(price)
            print(image_src)
            urlretrieve(image_src,"image/"+title+".png")
            print("="*50)


