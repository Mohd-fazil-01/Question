#Write a Python program that counts the number of words in a sentence where both the first and last letters are uppercase.

sentence = input("enter tha sentence = ")
new_sentence = sentence.split()
result = 0

for word in new_sentence:
    if len(word)>1 and word[0].isupper and word[-1].isupper():

        result += 1


print("your sentence is = ",sentence)
print("after spilt str is = ",new_sentence)
print("your answer is = ",result)
