n = input()
length = len(n)
sum = 0

# 왼쪽부분 자릿수 합 더하기
for i in range(length//2):
    sum += int(n[i])

# 오른쪽부분 자릿수 합 빼기
for i in range(length//2, length):
    sum -= int(n[i])

if sum == 0:
    print("LUCKY")
else : 
    print("READY")
