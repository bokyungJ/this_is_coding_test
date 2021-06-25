n,m = map(int, input().split())

card_list = [0]*n
num_list = [0]*n
for i in range(n):
    card_list[i] = list(map(int, input().split()))
    num_list[i] = min(card_list[i])
    
result = max(num_list)

print(num_list)
print(result)