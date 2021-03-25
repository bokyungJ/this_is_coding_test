# 실전문제) 두 배열의 원소 교체
# 내가 푼 것

n, k = map(int,input().split())

array_A = list(map(int,input().split()))
array_B = list(map(int,input().split()))

array_A.sort()
array_B.sort()

array = array_A+array_B

for i in range(k):
    if array_A[i]<array[len(array)-1-i]:
        array_A[i], array[len(array)-1-i] = array[len(array)-1-i], array_A[i]

print(sum(array_A))


