def solution(participant, completion):
    hash_dict = {}
    p_sum = 0
    c_sum = 0
    
    # participant list의 hash를 구하고 hash값을 더한다
    for p in participant:
        hash_dict[hash(p)] = p  # [1: 'A', 2: 'B', 3: 'C']
        p_sum += hash(p)   # p_sum = 1+2+3 = 6
    
    # completion의 해시값을 더한다
    for c in completion:  # [1: 'A', 3: 'C']
        c_sum += hash(c)  # 1+3 = 4
    
    # 둘의 차이를 구한다
    return hash_dict[p_sum - c_sum]