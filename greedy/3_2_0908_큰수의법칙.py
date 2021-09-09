n, m, k  = map(int,input().split())
num = list(map(int,input().split()))

num.sort()

result = 0

i = 0
j = 0
while(i != m):
    if j==k:
        result += num[-2]
        j=0
    else:
        result += num[-1]
    i+=1
    j+=1

print(n,m,k)
print(num)
print(result)