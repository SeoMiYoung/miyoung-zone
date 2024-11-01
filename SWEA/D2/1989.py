T = int(input())

for t in range(1, T+1):
	is_palindrome = 1
    
	get_str_arr = list(input()) # ['l', 'e', 'v', 'e', 'l']
	get_reversed_str_arr = get_str_arr[::-1]  # ['l', 'e', 'v', 'e', 'l']
	# print(f"원래: {get_str_arr}")
	# print(f"뒤집기: {get_reversed_str_arr}")
    
	for i in range(len(get_str_arr)):
		if get_str_arr[i] != get_reversed_str_arr[i]:
			is_palindrome = 0
  
	print(f"#{t} {is_palindrome}")
    