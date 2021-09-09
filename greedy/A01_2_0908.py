n = int(input())
num_list = list(map(int, input().split()))

num_list.sort(reverse=True)

count = 0

while(num_list):
    count +=1
    for _ in range(num_list[-1]):
        if num_list:
            num_list.pop()
        else:
            count -=1
            break
print(count)

# 3 -> 1 1 3
# 5 -> 1 1 1 1 1
# 5 -> 1 2 2 2 2
# 8 -> 4 3 3 3 3 3 3 3 