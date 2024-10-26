getNum = int(input())

for i in range(getNum):
    getInput = list(map(int, input().split()))
    getAvg = sum(getInput) / len(getInput)
    print(f"#{i+1} {round(getAvg)}")  