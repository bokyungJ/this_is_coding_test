N, M, K = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()

k = M//K
m = M%K

result = ((num_list[N-1]*K)*k)+(num_list[N-2]*m)

print(result)