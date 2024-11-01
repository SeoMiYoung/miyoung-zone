def setting(data):
    return data[1]

T = int(input())

for t in range(1, T+1):
	score_arr = []  # [학생번호, 총점] 넣기
	N, K = map(int, input().split())
	for i in range(1, N+1):
		get_score = list(map(int, input().split()))  # [87, 59, 88]
		get_total_score = round(get_score[0]*0.35 + get_score[1]*0.45 + get_score[2]*0.20, 4)
        
		score_arr.append([i, get_total_score])  
		# print(f"현재 상태 출력: {score_arr}")
        
	## [[1, 22], [2, 25], [3,11], [4,66]] 이런느낌으로 쌓였을 거임
    # 성적순으로 정렬
	sorted_score_arr = sorted(score_arr, key=setting, reverse=True)  # key에다가 정렬 기준 함수 제공
	# print(sorted_score_arr)
    
	index = -1
	for i, sublist in enumerate(sorted_score_arr):
		if sublist[0]==K:
			index = i
			# print(f"찾았습니다. 인덱스{i}에 있습니다.")
    
    # 등급 배열
	grade_arr = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
	# 등급 당 인원 수
	grade_limit_num = N//10
    
	# 등급 계산
	get_grade = grade_arr[index//grade_limit_num]
    
	print(f"#{t} {get_grade}")
    
    
