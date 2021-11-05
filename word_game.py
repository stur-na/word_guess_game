'''This project taught me about the open module and the readline method
and also the random shuffle method'''
#import the random shuffle module for shuffling the dictionary list
from random import shuffle

#Start game
def start_game():
    print('Welcome to the word guess game, guess a word from the dictionary')
    print('You have FIVE(5) guesses per round')
    while True:
        game()
        ahead = input('would you like to play again?\npress any key to continue or press the ENTER key to exit the game: ')
        if ahead:
            continue
        else:
            print('Goodbye!')
            break

#compare the user input with the computer word
def compare(ui, comp):
    if ui == comp:
        print('Hurray! you got the word correctly')
    else:
        print('Aw, you missed this time')
        print('The word was {}'.format(comp))

#logic
def game():
    count = 1
    score = 0
    wordlist = []
    with open(r"C:\Users\Cloud\Documents\python-tuts\engmix.txt", encoding="ANSI") as dic_file:
        wordlist = dic_file.readlines()
    shuffle(wordlist)
    for i in wordlist:
        userinput = input('Guess a word from the list: ')
        compare(userinput, i)
        count+=1
        if userinput == i:
            score+=1
        if count == 6:
            break
    print('you got {} word(s) correctly in this round'.format(score))

start_game()
