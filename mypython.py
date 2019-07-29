# #
# #
# # # WHICH WORD IS THE LONGEST?
#
# def find_longest_word(word_list):
#     longest_word = ''
#     for word in word_list:
#         if len(word) > len(longest_word):
#             longest_word = word
#     print longest_word
#
# words = raw_input('Please enter a word')
# word2 = raw_input("enter another word")
# word3 = raw_input("enter another word")
# word_list = words.split() + word2.split() + word3.split()
# find_longest_word(word_list)
#
#
# # #REVERSE ANY WORD
# def reverse_string(a_string):
#     return a_string[::-1]
#
# reverseWord = raw_input("Enter a word you would like to reverse")
#
# print (reverse_string(reverseWord))
#
# # #NAME GENERATOR
# firstName = raw_input("first name?")
# secondName = raw_input("second name?")
#
# print(firstName + " " + secondName)
#
#
# # #VOITING AGE
#
# ageStringVar = raw_input("age?")
# age = int(ageStringVar)
#
# if age > 17:
#     print("you can vote")
# else:
#     print ("you can't vote")
#
# # # # EQUAL OR UNEQUAL NUMBERS?
# number = raw_input("give me one number")
# number2 = raw_input("give me one number")
# num1 = int(number)
# num2 = int(number2)
#
# if number == number2:
#     print("equal numbers")
# else:
#     print("unequal numbers")
#
#
# # # WHAT IS THE BIGGEST NUMBER?
# number = raw_input("number?")
# number2 = raw_input("number?")
# number3 = raw_input("number?")
# num1 = int(number)
# num2 = int(number2)
# num3 = int(number3)
#
# if number > number2 > number3:
#     print(number)
# elif number2 > number > number3:
#     print(number2)
# elif number3 > number2 > number:
#     print(number3)
#
# # #ROCK, PAPER, SCISSORS GAME
# #
# rounds = raw_input("how many rounds do you want to play?")

# t = ["rock", "paper", "scissors"]
# computer = t[randint(0,2)]
#
# user1 = raw_input("rock, paper, scissors?")
# user2 = raw_input("rock, paper, scissors?")
#
# if user1 == "paper":
#     if user2 == "scissors":
#         print ("user1 loses!")
# if user1 == "paper":
#     if user2 == "rock":
#         print ("user1 wins!")
# if user1 == "rock":
#     if user2 == "paper":
#         print("user1 loses!")
# if user1 == "rock":
#     if user2 == "scissors":
#         print("user1 wins!")
# if user1 == "scissors":
#     if user2 == "paper":
#         print("user1 wins!")
# if user1 == "scissors":
#     if user2 == "rock":
#         print("user1 loses!")
# else:
#     print("Tie!")

#keep imports at top of the file
# import random
# number = random.randint(0,10)
#
# guess = int(raw_input("Guess a number between 0 and 10!"))
#
# while number != guess:
#     if guess > number:
#         print("your guess was bigger than the number!")
#     else:
#         print("your guess was smaller than the number!")
#     guess = int(raw_input("Guess a number between 0 and 10!"))
# print("you got it right!")

#BLACK JACK GAME breaks when over 21 or when you say n


def randomCard():
    import random
    card = random.randint(2,11)
    print("you drew a " + str(card))
    return card

drawCard = raw_input("draw a card")

score = 0
while True:
    if drawCard == "no":
        print(score)
        break
    elif drawCard == "yes":
        score = (randomCard() + score)
        print (score)
    if score > 21:
        print ("you LOSE!")
        break
    drawCard = raw_input("draw a card")






# write a program that generates a random number between 1-10
# contunually ask the user for guesses until they get it right
#tell user if they are too high or low
# while True:
#     name = raw_input("give me a name!")
#     if name == "stop":
#         break
#     print("name is " + name)

# Black Jack program
