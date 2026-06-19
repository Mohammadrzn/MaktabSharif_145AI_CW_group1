text = input('Enter a text').strip().lower()
vowels = 'aeiou'
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f'count of vowels{count}')