def check_palindrome():
    if text == text[::-1]:
        return 'Palindrome'
    else:
        return "not palindrome"
text = input("enter:")
print("original:", text)
print(check_palindrome())