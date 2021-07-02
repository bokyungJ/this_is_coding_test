'''
7,8,9,1
6,10,2
5,3
4
-> 7,8,9,1,6,10,2,5,3,4
'''

def solution(n):
    graph=[[0]*n for _ in range(n)]
    y = -1
    x = n-1
    num=1

    for i in range(n):
        for j in range(i,n):
            if i%3 == 0:
                y+=1
            elif i%3 == 1:
                x-=1
                y-=1
            elif i%3 == 2:
                x+=1
            graph[y][x] = num
            num+=1
    result = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                result.append(graph[i][j])
    return result
n = int(input())
print(solution(n))
