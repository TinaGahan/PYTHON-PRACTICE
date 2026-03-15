n = [1, 2, 3, 4, 5]
count1 = 0
count2 = 0
for i in n:
    if i % 2 == 0:
        count1 += 1
    else:
        count2 += 1
print("even:",count1)
print("odd:",count2)

