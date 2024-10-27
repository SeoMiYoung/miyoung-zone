iter_num = int(input())

for i in range(iter_num):
    P, Q, R, S, W = map(int, input().split())
    A_charge = 0
    B_charge = 0
    
    # A사인 경우 요금 계산
    A_charge = P*W
    
    # B사인 경우 요금 계산
    if W>R:
        B_charge = Q + (W-R)*S
    else:  # W<=R
        B_charge = Q
    
    print(f"#{i+1} {min(A_charge, B_charge)}")
