def solution(genres, plays):
    info_dict = {}
    
    for index, g in enumerate(genres):
        if g not in info_dict:
            info_dict[g] = {
                "plays": [[index, plays[index]]],
                "plays_sum": plays[index]
            }
        else:
            info_dict[g]["plays"].append([index, plays[index]])
            info_dict[g]["plays_sum"] += plays[index]
    # 현재 info_dict 상태: {'classic': {'plays': [[0, 500], [2, 150], [3, 800]], 'plays_sum': 1450}, 'pop': {'plays': [[1, 600], [4, 2500]], 'plays_sum': 3100}}
    
    
    #-----< 'plays'의 '회'에 따른 내림차순 정렬 >-----#
    for g in info_dict:
        info_dict[g]["plays"] = sorted(info_dict[g]["plays"], key=lambda x:-x[1])
    # 현재 info_dict 상태: {
    #   'classic': {
    #       'plays': [[3, 800], [0, 500], [2, 150]], 
    #       'plays_sum': 1450
    #    }, 
    #   'pop': {
    #       'plays': [[4, 2500], [1, 600]], 
    #       'plays_sum': 3100
    #    }
    # }
    
    #-----< 'plays_sum'에 따른 내림차순 정렬 >-----#
    # info_dict.items() --> dict_items([('classic', {내용}), ('pop', {내용})])
    # sorted를 썼으므로, list로 반환함
    ## info_dict_sorted = [('pop', {내용}), ('classic', {내용})]
    info_dict_sorted = sorted(info_dict.items(), key=lambda x:-x[1]["plays_sum"])
    ## 현재 info_dict_sorted 상태: [('pop', {'plays': [[4, 2500], [1, 600]], 'plays_sum': 3100}), ('classic', {'plays': [[3, 800], [0, 500], [2, 150]], 'plays_sum': 1450})]
    
    #-----< return 배열 만들기 >-----#
    return_arr = []
    for key, value in info_dict_sorted:
        return_arr.extend([p[0] for p in value["plays"][:2]])
    
    return return_arr