getNum = int(input())

for i in range(getNum):
    getInput = list(map(int, input().split()))
    getMax = max(getInput)
    print(f"#{i+1} {getMax}")