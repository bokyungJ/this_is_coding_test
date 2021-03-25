# 실전문제) 위에서 아래로
# 내가 푼 것

n = int(input())

array = []

for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

print(array)