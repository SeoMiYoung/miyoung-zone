getNum = int(input())
for _ in range(1, getNum+1):
    a, b = map(int,input().split())
    print(f"#{_}", end=' ')
    get_q = a//b
    get_r = a%b
    print(f"{get_q} {get_r}")