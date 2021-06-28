n = input()
n_list = []

for i in range(len(n)):
    n_list.append(int(n[i]))

result = n_list[0]
for i in range(1, len(n)):
    if n_list[i]==0 or result==0:
        result += n_list[i]
    else:
        result *= n_list[i]

print(result)