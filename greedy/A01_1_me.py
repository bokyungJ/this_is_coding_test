n = int(input())

n_list = list(map(int, input().split()))

n_list.sort()

count = 0
while n_list:
    count +=1
    for i in range(n_list[-1]): 
        n_list.pop()

print(count)