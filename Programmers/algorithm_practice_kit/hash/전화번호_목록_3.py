# sort, zip()를 적용함으로써 연산 줄이기

def solution(phone_book):
    check = True
    phone_book.sort()  # ["12", "6", "6789"]
    phone_book_zip = list(zip(phone_book, phone_book[1:]))  # [("12", "6"), ("6", "6789")]

    for p1, p2 in phone_book_zip:
        if p2.startswith(p1):
            check = False
    
    return check