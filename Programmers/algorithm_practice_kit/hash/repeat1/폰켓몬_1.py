from collections import Counter

def solution(nums):
    counts = Counter(nums)  # {'1': 1, '2': 1, '3': 2}
    counts_len = len(counts)
    
    if counts_len > (len(nums)//2):
        return len(nums)//2
    else:
        return counts_len