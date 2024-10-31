T = int(input())

for t in range(1, T+1):
	stk_arr = []
	for _ in range(9):
		stk_arr.append(list(map(int, input().split())))
	
    # 검증 과정
	test1_result = True  # (1) 가로 검사 통과 여부
	test2_result = True  # (2) 세로 검사 통과 여부
	test3_result = True  # (3) 네모 검사 통과 여부
    
    # (1) 가로 검사
	for i in stk_arr:
		test1 = set(i)
		if len(test1) != 9:
			test1_result = False
	
	# (2) 세로 검사
	for j in range(9):  # 열
		test2 = set()
		for i in range(9):  # 행
			test2.add(stk_arr[i][j])

		if len(test2) != 9:
			test2_result = False
            
	# (3) 네모 검사
	for i in range(0, 7, 3):  # 0, 3, 6 (행)
		for j in range(0, 7, 3):  # 0, 3, 6 (열)
			test3 = set()
            # 첫 줄
			test3.add(stk_arr[i][j])
			test3.add(stk_arr[i][j+1])
			test3.add(stk_arr[i][j+2])
			test3.add(stk_arr[i+1][j])
			test3.add(stk_arr[i+1][j+1])
			test3.add(stk_arr[i+1][j+2])
			test3.add(stk_arr[i+2][j])
			test3.add(stk_arr[i+2][j+1])
			test3.add(stk_arr[i+2][j+2])

			if len(test3) != 9:
				test3_result = False
     
	result = int(test1_result and test2_result and test3_result)
	print(f"#{t} {result}")