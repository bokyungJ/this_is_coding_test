n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0 # 총 그룹의 수
count = 0 # 그룹 속 팀원의 수

for i in data:
    count +=1
    if count>=i:
        result+=1
        count=0

print(result)