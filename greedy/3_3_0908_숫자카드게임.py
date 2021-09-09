n, m = map(int, input().split())

num_list = []
for _ in range(n):
    num = list(map(int, input().split()))
    num_list.append(min(num))

result = max(num_list)
print(result)