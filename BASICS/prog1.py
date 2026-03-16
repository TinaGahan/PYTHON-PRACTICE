n = input("ENTER NUMBER:")
if int(n) % 2 == 0:
    print("even")
else:
    print("odd")
total = 0
for i in n:
    total += int(i)
print("Total of digits:",total)
if n == n[::-1]:
    print("Palindrome")
else:
    print("not palindrome")