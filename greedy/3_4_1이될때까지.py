N , K = map(int,input().split())

count = 0 
while N !=1:
    if N%K == 0:
        N = N//K
        count +=1
    else : 
        N = N-1
        count +=1

print(count)

# 가능하면 많이 나누기