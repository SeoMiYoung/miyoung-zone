### 1번 방법
# 해당 방법도 pass했지만, 아무리도 이중 루프를 돌았기 때문에 시간 소요는 많이 됩니다. 

T = int(input())

for t in range(1, T+1):
	N = int(input())
	n_list = list(map(int, input().split()))   # [1, 1, 3, 1, 2]
    
	total = 0
	i = 0
	while i<N:
        ## 최대값에 해당하는 인덱스 찾기
		max_idx = i
		for m in range(i+1, N):
			if n_list[m] > n_list[max_idx]:
				max_idx = m
        
        ## 값 계산
		for v in range(i, max_idx):
			total += (n_list[max_idx] - n_list[v])
        
		i = max_idx + 1
	print(f"#{t} {total}")
