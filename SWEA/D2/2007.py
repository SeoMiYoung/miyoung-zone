T = int(input())

for t in range(1, T+1):
	get_str = input()  # 무조건 길이가 30인 문자열임
	r_n = 0
	for repeat_num in range(1, 11):  # 반복 가능한 길이 순회
        # repeat_num 만큼 반복된다는 가정하에, 예상 문자열 만들기
        # BLACKPINKBLACKPINKBLACKPINKBLA --> BLACKPINKBLACKPINKBLACKPINK 까지 만들기
		expected_arr = get_str[:repeat_num]*(30//repeat_num)
        
        # BLACKPINK/BLACKPINK/BLACKPINK/BLA
		if expected_arr == get_str[:repeat_num*(30//repeat_num)]:
			r_n = repeat_num
			break

	print(f"#{t} {r_n}")
        