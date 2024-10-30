T = int(input())
date_arr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(1, T+1):
	result = 0
	s_m, s_d, f_m, f_d = map(int, input().split())
    
	for m in range(s_m, f_m+1):
		if s_m == f_m:  # 시작과 끝 월이 똑같은 경우
			result = result + (f_d - s_d + 1)
		else:  # 시작과 끝 달이 다름
			if m == s_m:  # 시작 달이라면
				result = result + (date_arr[s_m]-s_d+1)
			elif m == f_m:  # 끝 달이라면
				result = result + f_d
			else:  # 그 사이
				result = result + date_arr[m]
		
	print(f"#{t} {result}")
    