T = int(input())

for t in range(1, T+1):
    N = int(input())
    num_arr = []
    num_arr_90 = []
    num_arr_180 = []
    num_arr_270 = []
    for n in range(N):
        num_arr.append(list(map(int, input().split())))
        num_arr_90.append([0]*N)
        num_arr_180.append([0]*N)
        num_arr_270.append([0]*N)
    
    '''
    num_arr_90 = [for i in range(N)]
    num_arr_180 = num_arr
    num_arr_270 = num_arr
    '''
    
    ## 90도 
    for i in range(N):  # 행
        for j in range(N):  # 열
            num_arr_90[j][N-1-i] = num_arr[i][j]

    ## 180도 
    for i in range(N):  # 행
        for j in range(N):  # 열
            num_arr_180[N-1-i][N-1-j] = num_arr[i][j]
            
    ## 270도 
    for i in range(N):  # 행
        for j in range(N):  # 열
            num_arr_270[N-1-j][i] = num_arr[i][j]
            
	# 출력
    print(f"#{t}")
    for i in range(N):
        for num in num_arr_90[i]:
            print(f"{num}", end='')
        print(" ", end='')
        
        for num in num_arr_180[i]:
            print(f"{num}", end='')
        print(" ", end='')
        
        for num in num_arr_270[i]:
            print(f"{num}", end='')
        print(" ", end='')
        
        print()