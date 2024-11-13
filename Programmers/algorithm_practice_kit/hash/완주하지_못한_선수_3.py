from collections import Counter

def solution(participant, completion):
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    
    result = list(p_counter - c_counter)
    return result[0]