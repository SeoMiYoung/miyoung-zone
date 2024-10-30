T = int(input())

for t in range(1, T+1):
	info_arr = []  # [['A', '10'], ['B', '7'], ['C', '5']]
	count_num = 0
    
	N = int(input())
	for n in range(1, N+1):
		get_arr = input().split()  # ['A', '10']
		info_arr.append(get_arr)

	# 출력
	print(f"#{t}")
	for k in info_arr:  # ['A', '10']
		while int(k[1]) != 0:
			count_num += 1
			print(f"{k[0]}", end='')
			k[1] = str(int(k[1])-1)
            
			if count_num%10 == 0:  # 10의 배수라면
				print()

	# 줄넘김
	print()
        
        
        