from itertools import combinations

n, m = map(int, input().split())
data = list(map(int,input().split()))

comb = len(list(combinations(data,2)))

data.sort()

count = 1
for i in range(len(data)-1):
    if data[i]==data[i+1]:
        count+=1
        if count>=2 and i+1==(len(data)-1):
            comb -= len(list(combinations(data[i+1-count:i+1],2)))
            count=1
    if count>=2 and data[i]!=data[i+1]:
        comb -= len(list(combinations(data[i+1-count:i+1],2)))
        count=1
print(comb)
