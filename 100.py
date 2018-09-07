from random import randint ; from string import ascii_letters ; from collections import Counter
l = list(ascii_letters)
newlist = []
for i in range(0,100):
        newlist.append(l[randint(1,51)])
print(Counter(newlist))