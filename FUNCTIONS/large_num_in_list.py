def is_largest():
    n = [56, 89, 32, 66, 87, 45]
    largest = n[0]
    for i in n:
        if i > largest:
            largest = i
    return largest
print(is_largest())

