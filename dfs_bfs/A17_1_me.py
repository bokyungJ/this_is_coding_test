# 못품
'''
n,k = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))

s,x,y = map(int, input().split())

da = [-1,1,0,0]
db = [0,0,-1,1]

count = 0 
def virus(a,b):
    global count
    count+=1
    for i in range(n):
        na = a+da[i]
        nb = b+db[i]
        if na>=0 and na<n and nb>=0 and nb<n:
            for j in range(k):
                if data[na][nb]==0:
                    if data[a][b] == j:
                        data[na][nb]=k
                        virus(na,nb)
while True:
    virus(0,0)
    if count == s:
        print(data[x-1][y-1])'''

from collections import deque

n,k = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
s,x,y = map(int, input().split())

da = [-1,1,0,0]
db = [0,0,-1,1]

q = deque()
q.append(data[0][0])

while q:
    now = q.popleft()

