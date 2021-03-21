# 예제 4-2) 시각
# 답안 예시

# 여기선 3중 반복문 사용
h = int(input())

count =0 
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각에 3이 포함되어있으면 count 증가
            if '3' in str(i)+str(j)+str(k):
                count +=1
print(count)