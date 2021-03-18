# 실전 3-2) 큰 수의 법칙
# 정답 예시

n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 반복되는 수열에 대해서 파악하자

# 가장 큰 수가 더해지는 횟수 계산
first_count = m//(k+1)*k + m%(k+1)

result = first_count*first + (m-first_count)*second
print(result)