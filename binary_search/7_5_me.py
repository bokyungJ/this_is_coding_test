# 실전문제) 부품찾기

n = int(input())
n_array = list(map(int,input().split()))
m = int(input())
m_array = list(map(int,input().split()))

array = []
for i in range(m):
    if m_array[i] in n_array:
        array.append('yes')
    else : 
        array.append('no')

for i in array:
    print(i, end=' ')