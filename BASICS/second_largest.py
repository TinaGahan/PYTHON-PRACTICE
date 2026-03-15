n  = [5, 8, 2, 10, 3]
s = maxx = n[0]
for i in n:
    if i > maxx:
        s = maxx
        maxx = i
        largest = maxx
        if i > s and i != largest:
            s = i
print(s)
