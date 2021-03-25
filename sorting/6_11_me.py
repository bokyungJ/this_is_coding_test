# 실전문제) 성적이 낮은 순서로 학생 출력
# 내가 푼 것 -> 못품

n = int(input())

array = []
for i in range(n):
    array.append(list(input().split()))

for i in range(n):
    array[i][1] = int(array[i][1])

print(array)

def setting(data):
    pass
array = sorted(array, key = setting)

print(array)