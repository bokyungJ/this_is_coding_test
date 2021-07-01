from itertools import combinations

money = int(input())
hamb = list(map(int, input().split()))
topp = list(map(int, input().split()))

for i in range(1, len(hamb)+1):
    data = [[0]*len(topp) for _ in range(i)]
    for j in range(i):
        hamb_temp = list(combinations(hamb,i))
        hamb
        for k in range(3):
            data[j][k] = 