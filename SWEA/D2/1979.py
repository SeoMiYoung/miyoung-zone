T = int(input())

for t in range(1, T+1):
	N, K = map(int, input().split())
	n_arr = []
    
    # 배열 채우기 (두 방향으로 빈 공간 한 줄 추가)
	for i in range(N):
		get_list = list(map(int, input().split()))  # [1, 1, 0, 1, 0, 1, 1, 1]
		get_list.append(0)  # [1, 1, 0, 1, 0, 1, 1, 1, 0]
		n_arr.append(get_list)
	n_arr.append([0]*(N+1))
  	
	result = 0
    # 가로 검사
	for i in range(N):
		count = 0
		for j in range(N+1):
			if n_arr[i][j] == 1:  # 갈 수 있는 구간
				count += 1
			else:  # 갈 수 없는 구간
				if count == K:
					result += 1
					count = 0
				else:
					count = 0
	
    # 세로 검사
	for j in range(N):
		count = 0
		for i in range(N+1):
			if n_arr[i][j] == 1:  # 갈 수 있는 구간
				count += 1
			else:  # 갈 수 없는 구간
				if count == K:
					result += 1
					count = 0
				else:
					count = 0
                    
	print(f"#{t} {result}")
    
        