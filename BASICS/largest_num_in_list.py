n = [5, 8, 2, 10, 3]
max_num = n[0]
for i in n:
    if max_num < i:
        max_num = i
print(max_num)