# 문제 : x만큼 간격이 있는 n개의 숫자

# 사용 문법
# range() : 반복 범위 생성
# append() : 리스트에 원소 추가
# for문 : 반복 수행

# 배운 점
# 규칙적으로 증가하는 수열은 반복문을 이용하여 쉽게 생성할 수 있다.
# x의 배수를 순서대로 구하면 x부터 x씩 증가하는 수열이 만들어진다.
# append()를 사용하여 계산한 값을 리스트에 차례대로 저장할 수 있다.

def solution(x, n):
    answer = []

    for i in range(1, n + 1):
        answer.append(x * i)

    return answer
