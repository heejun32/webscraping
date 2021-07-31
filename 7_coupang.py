'''
http method
get 방식:
post 방식
'''

import requests
from bs4 import BeautifulSoup
import re
url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
#print(items[0].find("div", attrs={'class':'name'}).get_text())

for item in items:
    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
    price = item.find("strong", attrs={"class":"price-value"}).get_text() #가격
    rate = item.find("em", attrs={"class":"rating"}) #가격
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) #평점수
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
    else:
        rate_cnt = "평점수 없음"
    print(name, price, rate, rate_cnt)

    # 이렇게 분기문을 추가해 원하는 정보를 얻을 수 있음.