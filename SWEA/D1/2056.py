getNum = int(input())
validDateArr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, getNum+1):
    getInput = input()
    getYear = getInput[0:4]  # '2000'
    getMonth = getInput[4:6]  # '11'
    getDate = getInput[6:]  # '24'
    
    # 유효성 검사
    if 1 <= int(getMonth) <= 12:  # 옳바른 달 입력
        if 1 <= int(getDate) <= validDateArr[int(getMonth)]:  # 옳바른 달 입력
            print(f"#{i} {getYear}/{getMonth}/{getDate}")
        else:
            print(f"#{i} -1")
    else:  # 옳바르지 않은 달 입력
        print(f"#{i} -1")