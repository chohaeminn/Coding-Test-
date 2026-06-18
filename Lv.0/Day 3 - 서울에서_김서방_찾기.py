# Day 3 - 서울에서 김서방 찾기
#
# 사용 문법
# - for
# - if
# - enumerate()
# - return
# - f-string
#
# 배운 점
# - enumerate()를 사용하면 리스트의 인덱스와 값을 동시에 가져올 수 있다.
# - 문자열 비교는 == 연산자를 사용한다.
# - 원하는 값을 찾으면 즉시 return으로 결과를 반환할 수 있다.
# - f-string을 사용하면 문자열 안에 변수를 쉽게 삽입할 수 있다.
#
# 추가 학습
# - enumerate(seoul)은 (인덱스, 값)을 반환한다.
# - f"문자열 {변수}" 형태로 문자열 포매팅이 가능하다.

def solution(seoul):
    for i, name in enumerate(seoul):
        if name == "Kim":
            return f"김서방은 {i}에 있다"
