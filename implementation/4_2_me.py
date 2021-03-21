# 예제 4-2) 시각
# 내가 푼 것

# 59분 59초까지니까
n = int(input())+1

hour, minute, second, count = 0,0,0,0

for i in range(60*60*n):
    second += 1
    if second == 60:
        second =0
        minute +=1
    if minute == 60:
        minute =0
        hour +=1
    # 시간 문자열로 만들기
    time = str(hour)+str(minute)+str(second)

    if '3' in time:
        count+=1 
# n이 2이면 2시 59분 59초까지 인데
# 지금은 3시 00분 00초까지 계산되어있음
# 그래서 하나 빼주기
if '3' in str(n):
    count -=1

print(count)