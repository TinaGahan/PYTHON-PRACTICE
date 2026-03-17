def is_palindrome():
    s = input("enter:")
    if s == s[::-1]:
        return "palindrome"
    else:
        return "not palindrome"
print(is_palindrome())

