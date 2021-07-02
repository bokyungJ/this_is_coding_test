'''
1
2,10
3,9,8
4,5,6,7
-> 1,2,10,3,9,8,4,5,6,7
'''
n = int(input())

def solution(n):
    graph = [[0]*n for i in range(n)]
    y=-1
    x=0
    num=1

    for i in range(n):
        for j in range(i, n):
            if i%3 == 0:
                y+=1
            elif i%3 == 1:
                x+=1
            elif i%3 == 2:
                y-=1
                x-=1
            graph[y][x]=num
            num+=1
    
    result = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] ==0:
                continue
            result.append(graph[i][j])
    
    return result
print(solution(4))