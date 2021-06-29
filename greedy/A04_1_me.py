# 못품 - 
from itertools import combinations

n = int(input())
num = list(map(int,input().split()))

num.sort()

new_list = []

for i in range(1,n+1):
    new_num = list(combinations(num,i))
    new_list.append()

max_num = max(new_list)
max_list = []
for i in range(1,max_num+1):
    max_list.append()

result_list = []
for data in max_list:
    if data not in new_list:
        result_list.append()

print(min(result_list))
'''