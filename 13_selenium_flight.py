from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options) #여기에 드라이버 경로 입력하기
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

# 가는날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번 달 28일
# browser.find_elements_by_link_text("28")[0].click() # [0] 이번달
# browser.find_elements_by_link_text("28")[0].click() # [0] 이번달

# time.sleep(1)
# browser.find_elements_by_link_text("29")[1].click() # [1] 다음달
# time.sleep(1)
# browser.find_elements_by_link_text("30")[1].click() # [1] 다음달

# 이번달부터 다음달까지
time.sleep(1)
browser.find_elements_by_link_text("29")[0].click() # [1] 다음달
time.sleep(1)
browser.find_elements_by_link_text("30")[1].click() # [1] 다음달

# 제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/span").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]"))
    # 성공했을 때 동작 수행
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()

# # 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)