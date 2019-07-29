## Background
'''
You've been brought on to build a game
to be featured for a new game show.
The game show will be fielding a variety
of games for its contestants - the one that
YOU are creating is a game where you have
to guess a word, letter by letter.
Sound familiar?
'''
## Task
'''
You will be creating a word guessing game.
A pre-set word is chosen, and the player
sees how many letters are in the word -
a blank spot for each letter.  The player
then has to guess the letters in the word,
one letter at a time. If the player guesses
a correct letter, then the correct letters
show in their respective spots. The letters
that the player has guessed should always be
 visible.
'''
'''
For example, if the word was "programming",
the player might see:
'''
import random

wordList = ["programming", "dogs", "cats", "turtles"]
word = random.choice(wordList)

numberOfDashes = int(len(word))
    

def spaces():
    len(word) = numberOfDashes
