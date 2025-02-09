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


#Count Names Containing At Least Two Capital Letters

sentence = "FAo zil FAfjh a Fdsf Fsd Djdfh DFjdfh Djk "
count = 0
two = 0
new_sentence = sentence.split()
print(new_sentence)
for n in new_sentence:
    for b in n:
        if b.isupper():
            two += 1
            if two == 2:
                count += 1
                break
        if b == n[-1]:
            two = 0       
print("your anaswer is =",count)    
