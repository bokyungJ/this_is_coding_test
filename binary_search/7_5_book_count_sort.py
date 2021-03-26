# 실전문제) 부품 찾기
# 답안 예시 - 계수 정렬

# N입력
n = int(input())
array = [0]*100001

# 가게에 있는 젠체 부품 번호를 받아서 기록
for i in input().split():
    array[int(i)] = 1

# M입력
m = int(input())
# 손님이 확인 요청한 거
x = list(map(int, input().split()))

# 손님이 확이 요청한 거 확인
for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else : 
        print('no', end=' ')