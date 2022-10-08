import random

word = "lick"
word_list = []
anagram = ""
new = []
length = len(word)
k = ""
for i in range(0, length):
    word_list.append(word[i])

print(word_list)
is_true = True
while is_true:
    k = random.choice(word_list)
    if k not in new:
        new.append(k)
        length -= 1
    if length == 0 :
        is_true = False
print(new)

#Need to alter for words with same letters; eg : "book"