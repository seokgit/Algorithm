import math
m, n = input().split()
m = int(m)
n = int(n)

for i in range(m, n+1):
    if i == 1:
        continue
    is_break = False
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_break = True
            break
    if is_break:
        continue
    print(i)