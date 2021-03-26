# 실전문제) 부품 찾기
# 답안 예시 - 집합 자료형

# N 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

# M 입력
m = int(input())
# 손님이 확인 요청한 거
x = list(map(int, input().split()))

# 손님이 확인 요청한거 확인
for i in x:
    if i in array:
        print('yes',end=' ')
    else : 
        print('no', end=' ')