# 실전 3-2) 큰 수의 법칙
# 단순하게 푸는 답안 예시

n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# k번만큼 first 더하고, second 더하자
result = 0
while True:
    for i in range(k): # 가장 큰 수 k번 더하기
        if m==0 : break
        result += first
        m -= 1
    if m==0 : break 
    result += second # 두 번째로 큰 수 한 번 더하기
    m -=1 

print(result)