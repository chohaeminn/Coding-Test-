# 문제 : 하샤드 수

# 사용 문법
# str() : 숫자를 문자열로 변환
# int() : 문자를 숫자로 변환
# for문 : 각 자릿수 순회
# % : 나머지 연산자

# 배운 점
# 정수를 문자열로 변환하면 각 자릿수를 하나씩 쉽게 확인할 수 있다.
# 자릿수의 합을 구한 뒤 원래 수가 그 합으로 나누어떨어지는지 확인하면 된다.
# 나누어떨어지는지 확인할 때는 나머지 연산자 %를 사용한다.

def solution(x):
    digit_sum = 0

    for i in str(x):
        digit_sum += int(i)

    if x % digit_sum == 0:
        return True
    else:
        return False
