
## Counting CONSONANTS(words without VOWEL) in given word

element = str(input("Enter a word: "))

word = element.lower()

vowel = ['a', 'e', 'i', 'o', 'u']

count = 0

# using for loop

for character in word:
    if character not in vowel:
        count += 1

print(count)
