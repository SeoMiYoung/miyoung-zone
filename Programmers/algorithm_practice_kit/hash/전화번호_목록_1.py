# 시간초과 났음

def solution(phone_book):
    check = True
    
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                check = False
            if phone_book[j].startswith(phone_book[i]):
                check = False
    
    return check