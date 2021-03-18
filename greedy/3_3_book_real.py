# 실전 3-3) 숫자 카드게임
# 정답 예시

# 카드 행, 열
n, m = map(int, input().split())

# 1. min() 함수 이용
result_min = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수들 중에서 큰 수 찾기
    result_min = max(result, min_value)
# 최종 답안 출력
print(result_min)

# 2. 2중 반복문 사용
result_for = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 장은 수 찾기
    min_value=100000
    for num in data:
        min_value = min(num,min_value)
    # 가장 작은 수들 중에서 큰 수 찾기
    result_for = max(result_for, min_value)
print(result_for)