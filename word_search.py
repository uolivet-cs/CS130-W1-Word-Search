''' This is a complete Python program. Read through it and make notes about
     its functionality. You are not expected to know what the program does.
     Simply use the context to reason out what you THINK is going to happen. '''

from random import randint

words_dct = dict()
with open('words_alpha.txt','r') as fp:
    for word in fp:
        word_start = word[0:3]
        if word_start not in words_dct:
            words_dct[word_start] = list()
        else:
            words_dct[word_start].append(word.strip())
    fp.close()

three_letters = input("Enter the first three letters of any word or 0 to quit: ")
while three_letters != '0':
    if three_letters in words_dct:
        num_words = len(words_dct[three_letters])
        if num_words > 1:
            print("Your search returns", num_words, "words.")
            user_choice = input("Press (1) to see a random word, or (2) to see all words: ")
            if user_choice == "1":
                print(words_dct[three_letters][randint(0,num_words)])
            else:
                print(', '.join(words_dct[three_letters]))
        elif num_words == 1:
            print("Your search returns 1 word:",words_dct[three_letters][0])
    else:
        print("Your search returns no words.")
    three_letters = input("Enter the first three letters of any word or 0 to quit: ")

print("Have a great day!")