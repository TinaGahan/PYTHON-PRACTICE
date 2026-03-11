def count_vowels(word):
    count = 0
    vowels = "aeiou"
    for ch in word:
        if ch in vowels:
            count += 1
    return count
print(count_vowels("programming in python"))


