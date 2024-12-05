def solution(phone_book):
    phone_book_dict = {}
    for i in phone_book: # O(1,000,000)
        # 어짜피 같은 전화번호는 중복되어있지 않음
        phone_book_dict[i] = 1  # 솔직히.. 굳이 1로 채울 필요가 없는 것 같은데.. 그냥 딕셔너리가 시간복잡도가 O(1)니깐 사용한듯?!?!
    
    # 정렬이 되면, 절대 뒷str가 앞str의 접두어가 될 수가 없음!
    # {"12": 1, "123": 1, "1235": 1, "567": 1, "88": 1}
    
    start = " "  # 그냥 ""로 하면, startswith() 다 통과됨..ㅎㅎ
    return_value = True
    for index, key in enumerate(dict(sorted(phone_book_dict.items()))):  
    # phone_book_dict.items(): dict_items([('12', 1), ('123', 1), ('1235', 1), ('567', 1), ('88', 1)])
    # sorted(phone_book_dict.items()): [('12', 1), ('123', 1), ('1235', 1), ('567', 1), ('88', 1)]
    # dict(sorted(phone_book_dict.items())): {'12': 1, '123': 1, '1235': 1, '567': 1, '88': 1}
        if key.startswith(start):
            return_value = False
        else:
            start = key
            
    return return_value