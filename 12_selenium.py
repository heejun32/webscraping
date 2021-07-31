import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options) #여기에 드라이버 경로 입력하기

# 1. 네이버로 이동
browser.get("http://naver.com")
browser.implicitly_wait(5)

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_xpath("//*[@id='account']/a")
elem.click()

# 3. 로그인 정보 입력
browser.find_element_by_id("id").send_keys("rlaskan95")
browser.find_element_by_id("pw").send_keys("spdlqjtlwkr2!")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()
browser.implicitly_wait(5)

# 5. id를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source) # 현 페이지의 모든 HTML 소스 출력

# 7. 브라우저 종료
#browser.close() #현재 탭만 종료
browser.quit() # 전체 브라우저 종료