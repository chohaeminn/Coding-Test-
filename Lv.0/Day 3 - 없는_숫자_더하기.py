# Day 3 - 없는 숫자 더하기
#
# 사용 문법
# - range()
# - not in
# - for
# - if
#
# 배운 점
# - 리스트에 없는 값을 찾을 때 not in 사용
# - 0~9 전체를 순회하며 없는 숫자를 찾을 수 있음
# - answer += i 로 합계를 누적할 수 있음

def solution(numbers):
    answer = 0

    for i in range(10):
        if i not in numbers:
            answer += i

    return answer
