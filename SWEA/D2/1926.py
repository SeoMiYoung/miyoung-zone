N = int(input())

for i in range(1, N+1):
	get_num_str = str(i)  # ex. "36", "30"
	if "3" in get_num_str or "6" in get_num_str or "9" in get_num_str:
		for n in get_num_str:  # "3" 들어오고 "6" 들어오고
			if int(n)==3 or int(n)==6 or int(n)==9:
				print("-", end='')
	else:
		print(f"{i}", end='')
	print(' ', end='')