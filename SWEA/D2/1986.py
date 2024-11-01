T = int(input())

for t in range(1, T+1):
	N = int(input())
    
	sum_n = 0
	for n in range(1, N+1):
		if n % 2 == 0:  # 짝수라면
			sum_n -= n
		else:  # 홀수라면
			sum_n += n

	print(f"#{t} {sum_n}")