from collections import Counter

def solution(participant, completion):
    participant_dict = Counter(participant)  # Counter({'ana': 1, 'mislav': 2, 'stanko': 1})
    completion_dict = Counter(completion)  # Counter({'ana': 1, 'mislav': 1, 'stanko': 1})
    
    for name in participant:
        if participant_dict[name] != completion_dict[name]:
            return name