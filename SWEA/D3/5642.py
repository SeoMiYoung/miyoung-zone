T = int(input())

for t in range(1, T+1):
	N = int(input())
	n_arr = list(map(int, input().split()))
    
    # 카데인 알고리즘
	localMaxValue = n_arr[0]
	globalMaxValue = n_arr[0]
	for i in range(1, N):
		localMaxValue = max(n_arr[i], localMaxValue + n_arr[i])
		# print(f"localMaxValue: {localMaxValue}")
		globalMaxValue = max(localMaxValue, globalMaxValue)
		# print(f"globalMaxValue: {globalMaxValue}")
  
	print(f"#{t} {globalMaxValue}")