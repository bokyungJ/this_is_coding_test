# 예제 3-1) 거스름돈
# 거슬러 줘야 할 동전의 최소 개수 (500원, 100원, 50원, 10원)

# 해결법 : 가장 큰 화폐의 단위부터 거슬러 주기

n=1260
count=0

# 큰 단위의 화폐부터 차례로 확인
coin_types=[500,100,50,10]

for coin in coin_types:
    num = n//coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    count += num
    #n -= (num*coin)
    n %= coin

print(count)