T = int(input())

for t in range(1, T+1):
	money = int(input())
	n_50000 = 0
	n_10000 = 0
	n_5000 = 0
	n_1000 = 0
	n_500 = 0
	n_100 = 0
	n_50 = 0
	n_10 = 0
    
    # 50000원
	while money//50000 != 0:
		n_50000 += money//50000
		money = money%50000
    
	# 10000원
	while money//10000 != 0:
		n_10000 += money//10000
		money = money%10000
        
	# 5000원
	while money//5000 != 0:
		n_5000 += money//5000
		money = money%5000

	# 1000원
	while money//1000 != 0:
		n_1000 += money//1000
		money = money%1000
        
	# 500원
	while money//500 != 0:
		n_500 += money//500
		money = money%500
     
	# 100원
	while money//100 != 0:
		n_100 += money//100
		money = money%100

	# 50원
	while money//50 != 0:
		n_50 += money//50
		money = money%50
        
	# 10원
	while money//10 != 0:
		n_10 += money//10
		money = money%10
       
	print(f"#{t}")
	print(f"{n_50000} {n_10000} {n_5000} {n_1000} {n_500} {n_100} {n_50} {n_10}")