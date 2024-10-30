T = int(input())

for t in range(1, T+1): 
	N, M = map(int, input().split())
    
	N_arr = list(map(int, input().split()))  # [1, 5, 3]
	M_arr = list(map(int, input().split()))  # [3, 6, -7, 5, 4]
    
	# 두 배열 중 더 길이가 긴 배열을 long_arr, 더 작은 배열을 short_arr로 저장
	if len(N_arr)>=len(M_arr):
		long_arr, short_arr = N_arr, M_arr  
		l_len, s_len = len(N_arr), len(M_arr)
	else:
		long_arr, short_arr = M_arr, N_arr
		l_len, s_len = len(M_arr), len(N_arr)
        
	max = -99999
	for i in range(0, l_len - s_len + 1):  # 0, 1, 2
		num_sum = 0
		for j in range(0, s_len):  # 0, 1, 2
			num_sum = num_sum + (short_arr[j] * long_arr[j+i])
            
		if num_sum > max:
			max = num_sum

	print(f"#{t} {max}")
        