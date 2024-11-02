T = int(input())

for t in range(1, T+1):
	a, b, goal = map(int, input().split())
	save_num = 1
	while True:
		if a < b:  
			a += b  # 더 큰 값을 더해준다
		else:
			b += a  # 더 큰 값을 더해준다

		if a > goal or b > goal:
			break
		else:
			save_num += 1
	print(f"{save_num}")
    