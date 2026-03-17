def sum_digit():
    n  = input("enter:")
    total = 0
    for i in n:
        total += int(i)
    return total
print(sum_digit())

