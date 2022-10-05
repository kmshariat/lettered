#importing random module to choose a random word from the list
import random

words = open ('words.txt','r') #opening the words file in read mode
wordList = list(x for x in words) #generating the list from txt file
word = random.choice(wordList)[:5].lower() #choosing a random word from the list and slicing the \n from the word

inputWord = input('Enter a four character word: ') #user input
inputWord.lower() #converting it to lower case

if word == inputWord:
    print(f'You win. The word is {word}')
else:
    print(f'The correct word is {word}')
