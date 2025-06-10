money = int(input())
list = list(map(int, input().split()))
bnp_money = money
timing_money = money
bnp_stock = 0
timing_stock = 0
up_cnt = 0
down_cnt = 0

for i in range(len(list)):
    if bnp_money >= list[i]:
        buy_cnt = int(bnp_money / list[i])
        bnp_stock += buy_cnt
        bnp_money -= buy_cnt * list[i]
    
    if list[i-1] < list[i]:
        up_cnt += 1
    else:
        up_cnt = 0
    if list[i-1] > list[i]:
        down_cnt += 1
    else:
        down_cnt = 0
    if up_cnt >= 3:
        timing_money += timing_stock * list[i]
        up_cnt = 0
    if down_cnt >= 3:
        buy_cnt = int(timing_money / list[i])
        timing_stock += buy_cnt
        timing_money -= buy_cnt * list[i]
        down_cnt = 0    

result1 = bnp_money + bnp_stock * list[-1]
result2 = timing_money + timing_stock * list[-1]

if result1 > result2:
    print("BNP")
elif result2 > result1:
    print("TIMING")
else:
    print("SAMESAME")