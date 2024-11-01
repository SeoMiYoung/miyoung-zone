T = int(input())

for t in range(1, T+1):
	N, M = map(int, input().split())
    
	##### 기본 배열 완성
	num_arr = [[0 for _ in range(N+1)] for _ in range(N+1)]  # (N+1)x(N+1) 배열
	for i in range(1, N+1):
		row = list(map(int, input().split()))  # [1,2,3,4,5]
		for j in range(1, N+1):
			num_arr[i][j] = row[j-1]
	# print(num_arr)
    
	###### 2차원 누적합 생성
	prefix_sum_arr = [[0 for _ in range(N+1)] for _ in range(N+1)] 
	for i in range(1, N+1):
		for j in range(1, N+1):
			prefix_sum_arr[i][j] = prefix_sum_arr[i-1][j] + prefix_sum_arr[i][j-1] - prefix_sum_arr[i-1][j-1] + num_arr[i][j]
	# print(prefix_sum_arr)
    
    ###### 최댓값 구하기
	max = -999
	for i in range(1, N-M+2):
		for j in range(1, N-M+2):
			result = prefix_sum_arr[i+(M-1)][j+(M-1)] - (prefix_sum_arr[i-1][j+(M-1)] + prefix_sum_arr[i+(M-1)][j-1]) + prefix_sum_arr[i-1][j-1]
			if result > max:
				max = result
  
	print(f"#{t} {max}")
            
        