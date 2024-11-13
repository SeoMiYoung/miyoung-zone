def solution(participant, completion):
    # 오름차순 정렬
    participant.sort()  # ['A', 'B', 'C']
    completion.sort()  # ['A', 'C']
    
    # 확인
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            return participant[i]
        
    return participant[len(participant)-1]