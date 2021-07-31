from bs4 import BeautifulSoup
import requests
import re

def create_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        }
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def print_news(index, title, link):
    print("{}. {}".format(index + 1, title))
    print("  (링크  : {})".format(link))

def get_weather():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)

    # 날씨 가져오기
    today_weather = soup.find("p", attrs={"class": "cast_txt"}).get_text()
    current_temperature = soup.find("span", attrs={"class": "todaytemp"}).get_text()
    max_temperature = soup.find("span", attrs={"class": "max"}).get_text()
    min_temperature = soup.find("span", attrs={"class": "min"}).get_text()
    morning_rain_rate = soup.find("span", attrs={"class": "point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class": "point_time afternoon"}).get_text().strip()

    dust = soup.find("dl", attrs={"class": "indicator"})
    fine_dust = dust.find_all("dd")[0].get_text()
    ultra_fine_dust = dust.find_all("dd")[1].get_text()

    print("[오늘의 날씨]")
    print(today_weather + '.')
    print("현재 {}℃  (최저 {} / 최고 {})".format(current_temperature, min_temperature, max_temperature))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(fine_dust))
    print("초미세먼지 {}".format(ultra_fine_dust))
    print()

def get_news():
    url = "https://news.naver.com/"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)

    print("[헤드라인 뉴스]")
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)
    print()

def get_news_it():
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    it_news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)

    print("[IT 뉴스]")
    for index, news in enumerate(it_news_list):
        title = news.find_all("a")[1].get_text().strip()
        link = news.find_all("a")[1]["href"]
        print_news(index, title, link)
    print()

def get_eng():
    print("[오늘의 영어회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english#;"
    soup = create_soup(url)

    sentences = soup.find_all("div", attrs={"class":"conv_txt"})
    eng_sentences = sentences[1].find_all("div", {"id":re.compile("^conv_kor_t")})
    kor_sentences = sentences[0].find_all("div", {"id":re.compile("^conv_kor_t")})

    print("(영어지문)")
    for sentence in eng_sentences:
        print(sentence.get_text().strip())
    print()
    print("(한글지문)")
    for sentence in kor_sentences:
        print(sentence.get_text().strip())
    print()

if __name__ == "__main__":
    get_weather()
    get_news()
    get_news_it()
    get_eng()