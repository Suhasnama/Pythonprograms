# tokenizer

# use python -V > 3.4


from nltk.tokenize import word_tokenize,sent_tokenize

import sys

from random import shuffle

def Tokenizing(text):

    # tokenizes into words
    if sys.argv[1] == "-w" :
        print(word_tokenize(text))
    
    # tokenizes into sentences
    elif sys.argv[1] == "-s":
        print(sent_tokenize(text))
    
    # shuffles the words 
    elif sys.argv[1] == "-r":
        list = word_tokenize(text)
        shuffle(list)
        for a in list:
            print(a ,end =" ")
    
    # displays the lexical diversity of every word in the text
    elif sys.argv[1] == "-L":
        list = word_tokenize(text)
        print("Lexical diversity of words is :"+ str(len(set(list))/len(list)))
    
    # displays the lexical diversity of every character in the text
    elif sys.argv[1] == "-l":
        print("Lexical diversity of characters is :"+str(len(set(text))/len(text)))

    # displays percentage of the given word in the text
    elif sys.argv[1] == "-p":
        if len(sys.argv)<4:
            print("Usage : nltk_test.py [-p] \"string\" key_word")
        else :
            list = word_tokenize(text)
            word = sys.argv[3]
            if word in list:
                print(str(100 * list.count(word) / len(list) ))
            else :
                print("Given word is not present in string")

    # displays usage of program
    else :
        print ("Usage: python nltk_test.py [-w / -s / -r / -l / -L / -p] string ")
        

def  main():
    if len(sys.argv)<2:
        print("Usage : python nltk_test.py [switch] \"string\" [key]")
    else :
        Tokenizing(sys.argv[2])    

if  __name__ == '__main__':
    main()