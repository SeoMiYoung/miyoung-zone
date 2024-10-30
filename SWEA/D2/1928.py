decode_arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

T = int(input())
for t in range(1, T+1):
    get_encoded_str = input()
    get_binary_str = ''  # 이진수 모아놓을 곳
    
    for i in get_encoded_str:  # 문자가 한개씩 들어옴
        get_index = decode_arr.index(i)  # 숫자가 나옴
        binary_num = bin(get_index)  # 숫자-->이진수
        binary_num = binary_num[2:]  # 앞에 0b 제거
        
        # 이진수 6자리 채우기
        while len(binary_num)!=6:
            binary_num = '0' + binary_num
        
        get_binary_str = get_binary_str + binary_num
     
    ##### 여기까지 이진수가 다 모아짐 #####
    # get_binary_str에는 문자열길이*6 만큼 저장되어있음
    
    result = ''  # 최종 결과 저장소
    for i in range(0, len(get_binary_str), 8):
        data = get_binary_str[i:i+8]
        
        if len(data)==8:
            result = result + chr(int(data, 2))
        else:
            result = result + chr(int(data.zfill(8), 2))
        
    print(f"#{t} {result}")
        
        
