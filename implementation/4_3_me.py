# 실전 4-3) 왕실의 나이트
# 내가 푼 것 

now = input()
x, y = now[0], int(now[1])

now_dict = {'a':1, 'b':2, 'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
x = now_dict[x]

# 이동할 수 있는 경우
move = ['lu','ld','ru','rd','ul','ur','dl','dr'] # 사실 이거 필요 없음 ㅋㅋㅋㅋ
dx = [-2,-2,2,2,-1,1,-1,1]
dy = [1,-1,1,-1,-2,-2,2,2]

count =0
for i in range(len(move)):
    nx = x+dx[i]
    ny = y+dy[i]
    if nx<1 or ny<1 or nx>8 or ny>8:
        continue
    count +=1

print(count)
