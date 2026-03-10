word = 'programming'
count = 0
vowels = 'aeiou'
for ch in  word:
    if ch in vowels:
        count += 1
print(count)