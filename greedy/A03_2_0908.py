s = input()
s_list = []

for i in range(len(s)):
    s_list.append(s[i])

count = 0

start = s_list[0]
for i in range(1, len(s)):
    if start != s_list[i]:
        start = s_list[i]
        count+=1

if count%2 == 0:
    count//=2
else:
    count=count//2+1
# 뭉테기 자체의 수 (000,111,00,11)를 구하면 홀짝나눌 필요 없음 count//=2
print(count)
