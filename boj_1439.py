s = input()
is_continue = False
start = -1
count = 0

for i in s:
    if start == -1:
        start = i
    if i == start:
        is_continue = False
    if i != start and not is_continue:
        count += 1
        is_continue = True

print(count)