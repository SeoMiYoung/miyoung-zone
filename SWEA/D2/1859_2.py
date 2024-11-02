T = int(input())

for t in range(1, T+1):
	N = int(input())
	n_list = list(map(int, input().split()))   # [1, 1, 3, 1, 2]
	n_list = n_list[::-1]  # [2, 1, 3, 1, 1]
    
	max_value = n_list[0]  # 2로 설정
	total = 0
	for i in range(1, N):
		if n_list[i] < max_value:
			total += (max_value - n_list[i])
		else:  # 새로운 최댓값 등장
			max_value = n_list[i]
            
	print(f"#{t} {total}")
