n = int(input())

n_list = []
n = str(n)
for i in n:
    n_list.append(int(i))

num = len(n)//2

n_1 = sum(n_list[:num])
n_2 = sum(n_list[num:])

if n_1 == n_2:
    print("LUCKY")
else : 
    print("READY")
