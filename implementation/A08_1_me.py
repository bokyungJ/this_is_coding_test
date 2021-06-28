input = input()

data = []
for i in input:
    data.append(i)

data.sort()

nums = '0123456789'

num = 0
result = ''
for i in data:
    if i in nums:
        i = int(i)
        num+=i
    else:
        result+=i

result += str(num)
print(result)