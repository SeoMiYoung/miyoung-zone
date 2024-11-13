def solution(nums):  # 배열이 들어온다는 뜻이구나..
    N = len(nums)  # 4
    N_2 = N//2  # 2
    
    if len(set(nums)) <= N_2:
        return len(set(nums))
    else:
        return N_2