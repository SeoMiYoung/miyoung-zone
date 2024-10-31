T = int(input())

for t in range(1, T+1):
    N = int(input())
    N_arr = list(map(int, input().split()))
    N_arr.sort()
    
    print(f"#{t}", end=' ')
    for i in N_arr:
        print(f"{i}", end=' ')
	
    print()