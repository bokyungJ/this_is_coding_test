# 실전 3-3) 숫자 카드게임
# 내가 푼 거

# 카드 행, 열
n, m = map(int, input().split())
# 각 숫자
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

# 각 행에서 가장 작은 숫자 배열 만들기
min_list = []
for i in range(n):
    min_list.append(min(data[i]))
print(min_list)

# 그 중 가장 큰 수 고르기
print(max(min_list))