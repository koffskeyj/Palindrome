import string
word = input("Please enter a word or statement: ").lower()
word = word.replace(" ", "")

for punct in string.punctuation:
    word = word.replace(punct, "")

i1 = 0
i2 = (len(word)-1)

while i1 < i2:
    c1 = word[i1]
    c2 = word[i2]
    if c1 == c2:
        i1 += 1
        i2 -= 1
    else:
        word = False
        print("Not a palindrome.")

print("Palindrome.")