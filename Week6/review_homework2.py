# 드림패스 내 포트폴리오 저장하기
from selenium import webdriver
import time
import config
# 웹 드라이버 켜기

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")

driver = webdriver.Chrome("./chromedriver")

driver.get("https://cdc.dongguk.edu/client/index.do")