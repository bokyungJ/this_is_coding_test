n, m = map(int, input().split())
x, y, d = map(int, input().split())

map_list = []
for i in range(n):
    map_list.append(list(map(int, input().split())))

# 북 서 남 동
dx = [-1,0,1,0]
dy = [0,-1,0,1]
moves = [0,3,2,1]
back_dx = [1,0,-1,0]
back_dy = [0,1,0,-1]

map_list[x][y] = 2

count = 1
cnt = 0 
while True:
    d = (d+1)%4
    nx = x+dx[d]
    ny = y+dy[d]
    if map_list[nx][ny] == 1 or map_list[nx][ny] == 2 or nx<0 or ny<0 or nx>n or ny>m:
        cnt+=1
        if cnt == 3:
            nx = x + back_dx[i]
            ny = y + back_dy[i]
            if map_list[nx][ny] == 1:
                break
    else : 
        map_list[nx][ny] = 2
        x = nx
        y = ny
        count +=1
        cnt = 0
print(count)