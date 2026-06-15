# 문제 : 두 정수 사이의 합

# 사용 문법
# range() : 특정 범위의 정수 생성
# min() : 두 수 중 작은 값 반환
# max() : 두 수 중 큰 값 반환
# for문 : 범위 내 숫자 순회
# += : 누적 합 계산

# 배운 점
# a와 b의 대소관계가 정해져 있지 않으므로 min(), max()를 사용하면 편리하다.
# range()의 끝값은 포함되지 않으므로 +1을 해주어야 한다.
# 반복문을 이용하여 범위 내 모든 정수의 합을 구할 수 있다.

def solution(a, b):
    answer = 0

    for i in range(min(a, b), max(a, b) + 1):
        answer += i

    return answer
