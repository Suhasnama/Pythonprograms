# imports tokenizers form nltk.tokenize ; shuffle from random
from nltk.tokenize  import word_tokenize, sent_tokenize
from random import shuffle

# takes input from user
example = input("Enter the text you like!\n")

# Uses this string as input 
# example = "Hello this is suhas. I'am new to python programming. I wish to learn NLP. I am using the nltk/book to learn NLP."

# declares an empty list
list = []

# stop_words = ["this","for","and","the","a","is","why"]

# tokenzies the input
list=word_tokenize(example)

# sorts the list
list.sort()

# shuffles the list 
shuffle(list)
#  = sorted(list , reverse:True)

# loops through the list and prints the elements of the list
for a in list:
    print(a ,end =" ")
