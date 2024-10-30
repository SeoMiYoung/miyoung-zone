T = int(input())

for t in range(1, T+1):
	value_arr = [[2,0], [3,0], [5,0], [7,0], [11,0]]
	num = int(input())
    
	for n in value_arr:  # n: [2,0]
		while num%n[0] == 0:
			n[1] += 1
			num = num // n[0]

	print(f"#{t} {value_arr[0][1]} {value_arr[1][1]} {value_arr[2][1]} {value_arr[3][1]} {value_arr[4][1]}")