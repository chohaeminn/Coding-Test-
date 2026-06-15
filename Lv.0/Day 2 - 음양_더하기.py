# 문제 : 음양 더하기

# 사용 문법
# len() : 리스트 길이 반환
# range() : 인덱스 반복
# if-else : 부호에 따라 처리
# +=, -= : 값 누적

# 배운 점
# 두 리스트를 같은 인덱스로 접근하면 서로 대응되는 값을 함께 처리할 수 있다.
# signs의 값이 True이면 양수, False이면 음수로 처리한다.
# 조건에 따라 더하거나 빼면서 최종 합계를 구할 수 있다.

def solution(absolutes, signs):
    total = 0

    for i in range(len(absolutes)):
        if signs[i]:
            total += absolutes[i]
        else:
            total -= absolutes[i]

    return total
