# 실전 3-2) 큰 수의 법칙
# 내가 푼거

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0
count = 0

for i in range(m):
    if count==k:
        result += second
        count= 0 
        continue
    result += first
    count +=1

print(result)
