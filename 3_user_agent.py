import requests
url = "http://google.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
res = requests.get(url, headers=headers)
# user_agent를 통해 제대로된 정보를 가져올 수 있음.

with open('mygoogle.html', 'w', encoding="utf-8") as f:
    f.write(res.text)

