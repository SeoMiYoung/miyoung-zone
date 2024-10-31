T = int(input())

for t in range(1, T+1):
	# print(f"{t}번째 진행 스타뜨!---------------------------")
	first_h, first_m, second_h, second_m = map(int, input().split())
    
	hour = first_h + second_h
	minute = first_m + second_m
    
	# 분에서 시간으로 빼낼 수 있나 확인
	if minute // 60 != 0:
		hour = hour + (minute // 60)
		minute = minute % 60
        
 	# 만약 시간이 12시간이 넘어가면?
	if hour > 12:
		if hour % 12 == 0:
			hour = 12
		else:
			hour = hour % 12 
        
	print(f"#{t} {hour} {minute}")
    
    