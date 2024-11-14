# sort를 적용함으로써 연산 줄이기

def solution(phone_book):
    check = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            check = False
    
    return check