n = int(input())
num = list(map(int, input().split()))
num.sort()

if num[0] > 1:
    result = 1

else:
    result = num[0]
    for i in range(1, len(num)):
        if result < num[i]:
            if result+1 == num[i]:
                result +=num[i]
            else:
                result += 1
                break
        else:
            result += num[i]
        if i == len(num)-1:
            result+=1


print(result)
        