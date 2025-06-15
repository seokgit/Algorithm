n = int(input())
include = [False]*(n+1)
d_list = []
max_weight = 0

for i in range(n):
    d_list.append(list(map(int, input().split())))

def back(i, weight): 
    global max_weight    
    if i >= n:
        max_weight = max(max_weight, weight)   
        return 
    else:
        if i + d_list[i][0] <= n:
            include[i] = True
            back(i+d_list[i][0], weight + d_list[i][1])
        include[i] = False
        back(i+1, weight)

back(0, max_weight)
print(max_weight)