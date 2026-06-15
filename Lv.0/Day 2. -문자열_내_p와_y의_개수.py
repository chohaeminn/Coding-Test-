# 문제 : 문자열 내 p와 y의 개수

# 사용 문법
# lower() : 문자열을 소문자로 변환
# count() : 특정 문자 개수 계산
# if-else : 조건에 따른 결과 반환

# 배운 점
# 대소문자를 구분하지 않는 비교는 lower() 또는 upper()를 사용하면 편리하다.
# count()를 사용하면 특정 문자의 개수를 쉽게 구할 수 있다.
# p와 y가 모두 없는 경우에도 count 결과가 0과 0이므로 True가 반환된다.

def solution(s):
    new_s = s.lower()

    if new_s.count('p') == new_s.count('y'):
        return True
    else:
        return False
