# 실전 5-10) 음료수 얼려먹기 -> dfs
# 내가 푼 것 -> 못품

# n,m 입력 받기
n, m = map(int, input().split())

graph = [[]*m for _ in range(n)]

for line in graph:
    line = input