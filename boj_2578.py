check_list = []
order_list = []
cnt = 0

for i in range(5):
    check_list.append(list(map(int, input().split())))

for i in range(5):
    order_list.append(list(map(int, input().split())))

for order in sum(order_list, []):
    check = 0
    cnt += 1
    for i in range(5):
        for j in range(5):            
            if check_list[i][j] == order:
                check_list[i][j] = 0                
    for list in check_list:
        if list.count(0) == 5:
            check += 1   
    for i in range(5):
        col_cnt = 0
        for j in range(5):
            if check_list[j][i] == 0:
                 col_cnt += 1
        if col_cnt == 5:
            check += 1
    d_cnt = 0
    for i in range(5):        
        if check_list[i][i] == 0:
            d_cnt += 1
        if d_cnt == 5:
            check += 1
    d2_cnt = 0            
    for i in range(5):        
        if check_list[i][4-i] == 0:
            d2_cnt += 1
        if d2_cnt == 5:
            check += 1
    if check >= 3:
        break                                         

print(cnt)