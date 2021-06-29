n = input()

count_list = []

# 연속되는 숫자의 개수 세기
count = 1
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        count+=1
    else:
        count_list.append(count)
        count = 1
count_list.append(count)

result = len(count_list)//2   
print(result)