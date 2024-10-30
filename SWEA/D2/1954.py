T = int(input())

for t in range(1, T+1):
	N = int(input())
    
    # 좌표
	y = 0
	x = 0
	num = 1
	d = [(1,0), (0,-1), (-1,0), (0,1)]

    # 표
	num_arr = []
	for _ in range(N):
		num_arr.append([0]*N)
        
    # print(num_arr)
    
    # 첫번째 줄 채우기
	for _ in range(0, N):  # 0~2
		num_arr[y][x] = num
		num += 1
		x = x + 1
    
	x = x - 1
    
    # 방향 꺾이는 구간 시작
    # 2 2 1 1
	d_count = 0  # 2가 되면 방향 전환
	d_count_goal = N-1
	d_count_goal_num = 0
	d_num = 0  # 방향 번호
	while num < (N*N+1):
		new_y = y + d[d_num % 4][0]
		new_x = x + d[d_num % 4][1]
		num_arr[new_y][new_x] = num
		d_count += 1
		num += 1
        
        # 새로운 y, x설정
		y, x = new_y, new_x
		# print(f"새로운 위치는 [{y}, {x}]입니다. 그리고 이제 그 다음에 {d_num} 방향으로 갑니다. [현재 상태] {num_arr}")
        
		if d_count == d_count_goal:
			d_num += 1  # 방향 전환
			d_count = 0  # 횟수 초기화
			d_count_goal_num += 1
            
		if d_count_goal_num == 2:
			d_count_goal -= 1
			d_count_goal_num = 0
	
    # 출력하기
	print(f"#{t}")
	for i in range(N):
		for j in range(N):
			print(num_arr[i][j], end=' ')
		print()