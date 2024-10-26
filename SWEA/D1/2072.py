inputNum = int(input())

for i in range(inputNum):
    getArr = list(map(int, input().split()))
    result = 0
    for ga in getArr:
        if ga % 2 != 0:
            result += ga
    print(f"#{i+1} {result}")
  