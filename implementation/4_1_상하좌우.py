n = int(input())
plan_list = list(input().split())

# L,R,U,D
dx = [0,0,-1,1]
dy = [-1,1,0,0]

x, y = 1,1

for i in plan_list:
    if i == 'L' :
        if y>1:
            y +=dy[0]
        else : 
            continue
    elif i == 'R' :
        if y<n:
            y +=dy[1]
        else:
            continue
    elif i == 'U' :
        if x>1:
            x +=dx[2]
        else:
            continue
    elif i == 'D' :
        if x<n:
            x+=dx[3]
        else:
            continue
    print(i)
    print(x,y)


print(x,y)