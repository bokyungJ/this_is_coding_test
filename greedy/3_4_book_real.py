# 실전 3-4) 1이 될 때까지
# 정답 예시

n,k = map(int, input().split())
result = 0

while True:
    # (n이 k의 배수)가 될 때까지 1씩 빼기
    target = (n//k)*k
    result += (n-target)
    n = target
    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n<k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)

# 간단한 방법보다 시간복잡도가 작아짐 -> log(N)