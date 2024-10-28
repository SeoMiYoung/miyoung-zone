T = int(input())

for i in range(1, T+1):
    # test_num 입력
    test_num = int(input())  # 1295
    
    # 기본 세팅
    seen_num = set()
    k = 1  # 곱해지는 값
    
    while len(seen_num) < 10:
        num = test_num * k
        seen_num.update(set(map(int, str(num)))) # {1, 2, 9, 5}추가
        # print(f"[num] {num} / [현재 seen_num상태] {seen_num}")
        k = k + 1
        
    print(f"#{i} {num}")