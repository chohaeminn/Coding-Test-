# Day 3 - 나누어 떨어지는 숫자 배열
#
# 사용 문법
# - for
# - if
# - %
# - append()
# - sort()
# - not
#
# 배운 점
# - % 연산자를 사용하여 나누어 떨어지는지 확인할 수 있다.
# - 조건에 맞는 값을 리스트에 append()로 추가할 수 있다.
# - 리스트가 비어있는지 확인할 때 if not 리스트를 사용할 수 있다.
# - sort()를 사용하여 리스트를 오름차순 정렬할 수 있다.
# - 조건에 맞는 값이 하나도 없으면 [-1]을 반환할 수 있다.

def solution(arr, divisor):
    answer = []

    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if not answer:
        answer.append(-1)

    answer.sort()
    return answer
