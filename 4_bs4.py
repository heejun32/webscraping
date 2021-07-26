import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # lxml은 구문 해석 파서
# print(soup.title.get_text())
# print(soup.a) soup 객체에서 처음 발견되는 a element 반환
# print(soup.a.attrs["href"]) # a 엘리먼트의 속성 정보를 출력(attrs)

print(soup.find("a", attrs={"class":"Nbtn_upload"}))