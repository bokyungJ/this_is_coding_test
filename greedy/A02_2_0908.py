S = input()
s_list = []

for i in range(len(S)):
    num = S[i]
    s_list.append(int(num))

result = s_list[0]
for i in range(1,len(s_list)):
    if result==0: # 1도 생각해주기
        result += s_list[i]
    else:
        result *= s_list[i]

print(result)

# 문자열은 마지막 '\n' 처리해줘야함