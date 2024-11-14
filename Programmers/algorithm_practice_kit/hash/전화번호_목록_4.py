# sort, zip()를 적용함으로써 연산 줄이기

def solution(phone_book):
    check = True
    phone_book.sort()  # ["12", "6", "6789"]
    hash_table = {}
    
    for i in phone_book:
        hash_table[i] = 1  # {"12":1, "6":1, "6789":1}

    for i in phone_book:
        jubdoo = ''
        for j in i:  # "12" -> "1", "2"
            jubdoo += j  # "1"
            if (jubdoo in hash_table) and (jubdoo != i):
                check = False
                break
    
    return check