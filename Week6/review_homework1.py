# 스타벅스 매장 찾기
from selenium import webdriver
import time

# 웹 드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
# 사이트 접속
driver.get("https://www.starbucks.co.kr/store/store_map.do/")

# city = input("시/도를 입력하세요 : ")
# address = input("구/군을 입력하세요 : ")
city = "서울"
address = "서대문구"

locationSearch = driver.find_element_by_css_selector("h3.on")
locationSearch.click()

searchBox = driver.find_element_by_css_selector("article.store_map_layer_cont")
location_list = searchBox.find_elements_by_css_selector("a.set_sido_cd_btn")
print(location_list)
# searchBox.send_keys(city+" "+address)