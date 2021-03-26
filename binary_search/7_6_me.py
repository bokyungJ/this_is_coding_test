# 3.실전문제) 떡볶이 떡 만들기
# 내가 푼 것 -> 재귀함수 사용
n, m = map(int, input().split())
array = list(map(int, input().split()))

h = sum(array)//len(array)

def cutting(array, n,h,m):
    hap = 0
    for i in range(n):
        num = array[i]-h
        if num < 0 :
            num = 0
        else:
            hap+=num
    if hap == m:
        return h
    elif hap > m :
        return cutting(array, n, h+1,m)
    else :
        return cutting(array, n, h-1,m)

print(cutting(array, n,h,m))