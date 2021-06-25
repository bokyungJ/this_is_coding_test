# 못품

n = int(input())
count =0 
time = 0 
for hour in range(n+1):
    for min in range(60):
        for sec in range(60):
            if sec < 10:
                if str(sec) == '3':
                    count +=1
            else :
                if str(sec)[0] or str(sec)[1] =='3':
                    count += 1
        if min < 10:
            if str(min) == '3':
                count +=1
        else :
            if str(min)[0] or str(min)[1] =='3':
                count += 1
    if hour < 10:
        if str(hour)=='3':
            count+=1
    else:
        if str(hour)[0] =='3' or str(hour)[1]=='3':
            count+=1

print(count)