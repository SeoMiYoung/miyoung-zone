T = int(input())  # T개의 test case 존재

for t in range(1, T+1):
    test_num = int(input())  # 테스트 번호 입력받기
    test_list = list(map(int, input().split()))  # 숫자 리스트
    
    grade_count_arr = [0]*101  # 총 0점~100점 --> 101칸의 가능 점수
    
    # grade_count_arr 를 순회하면서 각 등급이 나온 횟수 저장
    for i in test_list:
        grade_count_arr[i] += 1
    #----------- 모든 등급의 갯수를 셈
    
    # 최빈값 찾기
    max_index = 0  # max값이 저장된 인덱스 저장
    for i in range(len(grade_count_arr)):  # i: 0~100
        if grade_count_arr[i] >= grade_count_arr[max_index]:  # 새로운 탐색값이 더 큰 경우
            max_index = i
 
    print(f"#{test_num} {max_index}")
            
            
        
        
    