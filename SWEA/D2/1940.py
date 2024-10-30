T = int(input())

for t in range(1, T+1):
	N = int(input())
    
	fast_state = 0
	result = 0
    
	for _ in range(1, N+1):  # 2번 입력을 받는다
		cmd_list = list(map(int, input().split()))  # [1, 2]
		cmd_num = 0
		cmd_value = 0
        
		if len(cmd_list)==2:
			cmd_num = cmd_list[0]
			cmd_value = cmd_list[1]
		else:
			cmd_num = cmd_list[0]
        
        # 속도 계산
		if cmd_num == 0:
			fast_state = fast_state  # 현재 상태 유지
		elif cmd_num == 1:  # 가속
			fast_state = fast_state + cmd_value
		else:  # 감속
			fast_state = fast_state - cmd_value
			if fast_state<0:
				fast_state = 0
     
		# print(f"값 추가: {fast_state}")
		result = result + (fast_state * 1)  # 1초 시간에 대한 거리 계산
	
	print(f"#{t} {result}")
        
        
    