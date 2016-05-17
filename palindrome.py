import string

word = input("Please input word or statement: ").lower()
word = word.replace(" ", "")

for c in string.punctuation:
    word = word.replace(c, "")

if word[0:] == word[::-1]:
    print("Palindrome!")
else:
    print("Not a palindrome!")

