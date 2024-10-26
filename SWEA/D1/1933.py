getNum = int(input())

for i in range(1, getNum+1):
    if getNum % i == 0:
        print(i, end=' ')