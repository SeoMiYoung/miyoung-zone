A, B = map(int, input().split())

if ((A==3 and B==2) or (A==1 and B==3) or (A==2 or B==1)): # A가 이기는 경우
    print("A")
else:
    print("B")