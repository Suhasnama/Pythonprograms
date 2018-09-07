word = input("Enter a word\n")
dict = {}
dict["words"] = len(word)

dict["vovels"] = 0

for i in word:
    if i in ['a','e','i','o','u']:
        dict["vovels"] = dict["vovels"] + 1

dict["percentage"] = dict["vovels"]/dict["words"]

print(dict)