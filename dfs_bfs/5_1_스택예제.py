stack = []

# 5-2-3-7-()-1-4-()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 5231
print(stack[::-1]) #1325 