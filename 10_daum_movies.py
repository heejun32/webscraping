import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=2018%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

images = soup.find_all("img", attrs={"class":"thumb_img"})


for year in range(2015, 2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    images = soup.find_all("img", attrs={"class": "thumb_img"})
    print(images)
    # for idx, image in enumerate(images): # 이거 공부하기
    #     image_url = image['src']
    #     if image_url.startswith("//"):
    #         image_url = "https:" + image_url
    #
    #     image_res = requests.get(image_url)
    #     image_res.raise_for_status()
    #
    #     with open("movie_{}_{}.jpg".format(year, idx+1), 'wb') as f:
    #         f.write(image_res.content)
    #
    #     if idx >=4:
    #         break