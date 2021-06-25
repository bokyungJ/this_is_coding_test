now = input()
now_list = []

cols = 'abcdefgh'
for i in range(len(cols)):
    if now[0] == cols[i]:
        now_list.append(i+1)
        now_list.append(int(now[1]))

# 우우상, 우우하, 좌좌상, 좌좌하, 상상좌, 상상우, 하하좌, 하하우
dx = [2, 2, -2, -2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

count =0

for i in range(8):
    nx = now_list[0]+dx[i]
    ny = now_list[1]+dy[i]
    if nx<1 or ny<1 or nx>8 or ny>8:
        continue
    else:
        count +=1
print(count)

