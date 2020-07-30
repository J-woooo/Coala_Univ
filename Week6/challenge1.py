# 파파고로 영단어 해석하기 번역결과 출력

from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("https://papago.naver.com")

time.sleep(1)

input_box = driver.find_element_by_css_selector("textarea#txtSource")
input_box.send_keys("seize the day")

button = driver.find_element_by_css_selector("button#btnTranslate")
button.click()

time.sleep(0.5)
result = driver.find_element_by_css_selector("div#txtTarget").text
print(result)