from selenium import webdriver
import time

# 웹 드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
# 네이버 지도 접속하기
driver.get("https://v4.map.naver.com/")
# 검색창에 검색어 입력하기  //검색창: input#search-input
searchBox = driver.find_element_by_css_selector("input#search-input")
searchBox.send_keys("치킨")
# 검색버튼 누르기 // 검색버튼: button.spm

# 지연시간 주기

searchButton = driver.find_element_by_css_selector("button.spm")
searchButton.click()
# 검색 결과 확인하기

time.sleep(1)

# 컨테이너 
stores = driver.find_elements_by_css_selector("dl.lsnx_det")
for store in stores:
    name = store.find_element_by_css_selector("dt > a").text
    address = store.find_element_by_css_selector("dt.addr").text
    tel = store.find_element_by_css_selector("dd.tel").text
    print(name)
    print(address)
    print(tel)

page_bar = driver.find_elements_by_css_selector("div.paginate > *")
page_bar[2].click()