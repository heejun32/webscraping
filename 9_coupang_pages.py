import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

for i in range(1, 6):
    url = "https://www.coupang.com/np/search?rocketAll=false&q=%EB%85%B8%ED%8A%B8%EB%B6%81&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page={}&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&component=&rating=0&sorter=scoreDesc&listSize=36".format(i)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    print("\n" + "페이지 " + str(i))

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