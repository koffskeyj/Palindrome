import string
word = input("Please enter a word or statement: ").lower()
word = word.replace(" ", "")

for punct in string.punctuation:
    word = word.replace(punct, "")
i1 = 0
i2 = -1

if len(word) <= 1:
    print("Palindrome.")

c1 = word[i1]
c2 = word[i2]

if c1 == c2:
    i1 += 1
    i2 += -1
    print("Palindrome")
elif i1 != i2:
    print("Not a Palindrome")
