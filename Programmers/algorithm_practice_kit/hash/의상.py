def solution(clothes):  
    # [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    
    dict_arr = {}
    for item, type in clothes:  # item: "yellow_hat", type: "headgear"
        if type not in dict_arr:  # 만약에 새로운 type 이라면
            dict_arr[type] = 1
        else:  # 기존에 있던 type
            dict_arr[type] += 1
    ###### {"headgear":2, "eyewear":1}
    
    # value값들을 한개씩 더해서 다 곱한다음 -1하면 됨
    result_sum = 1
    for v in dict_arr.values():
        result_sum = result_sum * (v+1)
    result = result_sum - 1
    
    return result
        