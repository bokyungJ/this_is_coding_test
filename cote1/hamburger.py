'''
햄버거 1개 이상, 토핑 최대 2개(같은 토핑 여러번x)
최대한 용돈 많이 썼을 때 지출 금액
아무것도 못사면 -1리턴
'''
# 못품
from itertools import combinations

money = int(input())
hamburg = list(map(int, input().split()))
hamburg.sort()
topping = list(map(int, input().split()))

# 토핑 최대 두개 -> 조합으로 2개 더한 값 토핑 리스트에 추가
topping_list = list(combinations(topping,2))
for i in range(len(topping_list)):
    topping.append(sum(topping_list[i]))

money_list = []

for i in range(1, len(hamburg)+1):
    # 1부터 조합으로 햄버거 더한 값 햄버거 리스트에 추가
    hamburg_list = []
    temp_list = list(combinations(hamburg,i))
    for j in range(len(temp_list)):
        hamburg_list.append(sum(temp_list[j]))
    # 햄버거 리스트에 있는 가격이랑 토핑*햄버거개수 가격 더해서 리스트 작성
    for k in hamburg_list:
        for p in topping:
            money_list.append(k+(p*i))

money_list.sort()
print(money_list)
for i in range(len(money_list)):
    if money_list[i]>=money:
        if money_list[i] == money:
            result = money_list[i]
        else:
            result = money_list[i-1]
        break

print(result)