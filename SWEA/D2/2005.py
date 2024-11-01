T = int(input())

for t in range(1, T+1):
	N = int(input())
    
	num_arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
	num_arr[1][1] = 1
    
    # 계산 스타트
	for i in range(2, N+1):
		for j in range(1, i+1):
			num_arr[i][j] = num_arr[i-1][j-1] + num_arr[i-1][j]
            
	# 출력
	print(f"#{t}")
	for i in range(1, N+1):
		for j in range(1, i+1):
			print(num_arr[i][j], end=' ')
		print()