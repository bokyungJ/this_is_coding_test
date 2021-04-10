# 실전) 1로 만들기
# 내가 푼거 - 모르겠음

# n 입력
n = int(input())

def cal(x):
    count=0
    while(x!=1):
        count+=1
        if x%5 == 0:
            x//5
        elif x%3 == 0:
            x//3
        elif x%2 ==0:
            x//2
        else:
            x-=1
    return count

print(cal(n))