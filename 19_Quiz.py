from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 창 최대화

# 1. 브라우저 시작
url = "http://naver.com"
browser.get(url)
browser.implicitly_wait(3)

# 2. 브라우저 "헬리오 시티 검색"
browser.find_element_by_id("query").click()
browser.find_element_by_id("query").send_keys("송파 헬리오시티")
browser.find_element_by_class_name("ico_search_submit").click()
browser.implicitly_wait(3)

# 3. 매물 정보로 페이지로 이동
browser.find_element_by_class_name("api_more_theme").click()
# browser.implicitly_wait(10)
# browser.find_element_by_link_text("동일매물 묶기").click() 동일 매물 묶기는 나중에 구현해보기

browser.find_element_by_class_name("item_area").clck().execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2  # 2초에 한번씩 스크롤 내림
# 현재 문서 높이를 가져와서 저장
prev_height = browser.find_element_by_class_name("item_area").execute_script("return document.body.scrollHeight")

while True:
    browser.find_element_by_class_name("item_area").execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)
    # 현재 문서 높이를 가져와서 저장
    current_heigth = browser.find_element_by_class_name("item_area").execute_script("return document.body.scrollHeight")
    if current_heigth == prev_height:
        break

    prev_height = current_heigth

print("scroll 완료")

