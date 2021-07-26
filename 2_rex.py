import re # 정규식 라이브러리

p = re.compile("ca.e") # 원하는 정규식을 컴파일 함.
# . 하나의 문자 의미
# ^ 시작 문자 설정
# $ 끝 문자 설정

m = p.match("caffe") # 주어진 문자열이 처음부터 일치하는지 확인
# print(m.group())    # 매치되지 않으면 에러가 발생

if m:
    print(m.group())
else:
    print("매칭되지 않음.")

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# . 하나의 문자 의미
# ^ 시작 문자 설정
# $ 끝 문자 설정