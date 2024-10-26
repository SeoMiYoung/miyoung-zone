getArr = list(map(int, input().split(' ')))

# 오름차순 정렬
getArr.sort()

# 중간값에 해당하는 인덱스
middleIdx = len(getArr)//2

print(getArr[middleIdx])