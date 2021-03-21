# 예제 4-1) 상하좌우
# 내가 푼 것

# 공간의 크기를 나타내는 N
n = int(input())

# 계획서
plan = list(input().split())

# 처음 좌표
x,y = 1,1

for i in range(len(plan)):
    if plan[i] =='R':
        if y == n:
            y=n
        else : 
            y+=1
    elif plan[i] == 'L':
        if y==1 :
            y=1
        else : 
            y-=1
    elif plan[i] =='U':
        if x ==1:
            x=1
        else : 
            x -=1
    elif plan[i] =='D':
        if x==n:
            x=n
        else:
            x +=1

print("%d %d" %(x,y)) 
