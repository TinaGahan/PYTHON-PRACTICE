def is_second_largest():
    n = [56, 89, 32, 66, 87, 45]
    largest = n[0]
    second_largest = n[0]
    for i in n:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i != largest:
                second_largest = i
    return second_largest
print(is_second_largest())