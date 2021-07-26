import requests
#res = requests.get("http://naver.com")
res = requests.get("http://google.com")

print("응답코드 :", res.status_code)


res.raise_for_status() # html 코드 제대로 가져왔는지 확인. # 오류 내뱉고 프로그램 종료
print("웹 스크래핑 진행")
print(len(res.text))

with open('mygoogle.html', 'w', encoding="utf-8") as f:
    f.write(res.text)

