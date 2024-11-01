T = int(input())

for t in range(1, T+1):
    num_list = list(map(int, input().split()))
    num_list.sort()  # 오름차순(원본 변경)
    # print(f"오름차순: {num_list}")
    num_list_cut = num_list[1:len(num_list)-1]
    # print(f"오름차순 cut: {num_list_cut}")
    calculate_avg = round(sum(num_list_cut)/len(num_list_cut))
    
    print(f"#{t} {calculate_avg}")