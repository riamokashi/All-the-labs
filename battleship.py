# #
# # # Simplified Battleship!
# # import random
# # import sys
# #
# # SEA_LENGTH = 20
# # SHIP_LENGTH = 3
# # SHIP_COUNT = 3
# # HASHES_STRING = '#' * (SEA_LENGTH+2)
# # MAX_RETRIES = 1000
# #
# # def isValidPlacement(sea, index):
# #     if index < 0 or index > SEA_LENGTH - SHIP_LENGTH:
# #         return False
# #
# #     for i in range(SHIP_LENGTH):
# #         if (sea[index + i] == '*'):
# #             return False
# #     return True
# #
# #
# # def generateShipPlacements(sea_length, ship_length, ship_count):
# #   # FYI: lines 9-11 can be shortened to a 'list comprehension' via
# #   # array = [0 for i in range(sea_length)]
# #   # but we haven't covered this shorthand :)
# #   sea = []
# #   for i in range(sea_length):
# #     sea.append('0')
# #
# #   # now that we have our sea, let's fill it with a ship
# #   count = 0
# #   retries = 0
# #   while count < SHIP_COUNT and retries < MAX_RETRIES:
# #       rand_index = random.randint(0, len(sea) - SHIP_LENGTH)
# #       if isValidPlacement(sea, rand_index):
# #           count += 1
# #           for i in range(SHIP_LENGTH):
# #               sea[rand_index + i] = '*'
# #       else:
# #           retries += 1
# #   return sea
# #
# # def printSea(sea):
# #     print(HASHES_STRING)
# #     sys.stdout.write('#')
# #     for i in sea:
# #         sys.stdout.write(i)
# #     print '#'
# #     print(HASHES_STRING)
# #
# # '''
# # Battleship is a game where you attempt to discover your opponent's ship locations in a hidden sea.
# #
# # The player has a matching 'sea' where they can track previous attempts to discover a ship.
# #
# # If a player successfully guesses the location of a ship, the opponent must tell them so that the player can use that information to guess future shots. This is what the player 'sea' board is for.
# #
# # Objective:
# #  Continually ask the user to shoot a slot with a missile
# #  If it is a hit, mark that index in 'player_sea' with a *
# #  If it is a miss, mark that index in the 'player_sea' with a
# #  X so they know not to shoot there again!
# #  End the game when all 'ships' have been 'sunk'
# #  (when all '*'s in the player_sea board map to the '*'s in
# #  the 'opponent_sea')
# #  After each choice, you should reprint the player_sea
# #  array using printSea function defined above
# #
# #  STRETCH: Implement the computer AI to take its turn after each choice you make and see who wins.
# # '''
# #
# # ########################################
# # #      YOUR CODE BELOW THIS LINE       #
# # ########################################
# #
# # '''
# # Q: What are your milestones?
# # A: ...
# #
# #
# #
# # #7: write a function that checks if player_sea has hit all of the ships in opponent_sea
# # '''
# # # this represents the 'hidden' board that you are attempting to shoot
# # opponent_sea = generateShipPlacements(SEA_LENGTH, SHIP_LENGTH, SHIP_COUNT)
# #
# # # this represents the players board which tracks where you
# # # have previously attempted to shoot
# #
# # player_sea = ['-' for i in range(SEA_LENGTH)]
# #
# # while True:
# #     print(player_sea)
# #     userGuess = int(raw_input("choose the index where you will shoot or enter 100 to quit"))
# #     if userGuess == 100:
# #             break
# #     elif userGuess > SEA_LENGTH or userGuess < 0:
# #         print("you are out of range, pick a number that is within the " + str(SEA_LENGTH))
# #     elif "*" == opponent_sea[userGuess]:
# #         player_sea[userGuess] = "*"
# #     elif "x" == player_sea[userGuess] or "*" == player_sea[userGuess]:
# #         print("you already guessed that")
# #     elif player_sea.count("*") == opponent_sea.count("*"):
# #         print("you win!")
# #         break
# #     else:
# #         player_sea[userGuess] = "x"
#
# # state1 = "New York"
# # abbr1 = "NY"
# # state2 = "California"
# # abbr2 = "CA"
# #
# # print(abbr2 + " is short for " + state2)
# #
# #
# # # states = ["CA = California", "NY = New York"]
# # states_abbr = ["CA", "NY"]
# # states = ["california", "new york"]
# # for index in range(len(states)):
# #     print(states_abbr[index] + " is short for " + states[index])
# #
# #
# states = {
# "NY": "New York",
# "MI": "Michigan",
# "FL": "Florida"
# }
#
# pet = {
#     'name': 'Skeemer',
#     'animal': 'dog',
#     'breed': 'bichon frise',
#     'age': 16
# }
#
# #MODIFY
# # print(pet['name'] + ' has disassociated himself from the walshes and shall now be known as ')
# # pet['name'] = 'Simba'
# # print(' and shall now be known as ' + pet['name'])
#
# #ADD
# pet['favorite'] = 'milkbone'
# print(pet['favorite'])
#
#
# #REMOVE
# print(pet)
# pet.pop('age')
# print(pet)
# for open in states:
#     print("key is " + open)
#     print("value is " + states[open])
#
# pets = [
#     pet,
#     {
#     'name': 'Michael',
#     'age': 5
#     }
# ]

class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("ruff ruff ruff!!")

my_pet = Pet("Finn", 14)

print("my new pet is " + my_pet.name + " and he/she is " + str(my_pet.age))
my_pet.bark()

# print(pets)
#
#
#
# # food = {
# # "good": "pizza",
# # "great": "pasta",
# # "amazing": "tiramisu"
# # }
# #
# # for rank in food:
# #     print("the rank is " + rank)
# #     print("the food is " + food[rank])

# roberts_life = {
#     'name': 'robert',
#     'age': 17,
#     'movies': {
#         'name': 'Avenger\'s End Game',
#         'rating': 'PG-13',
#     }
# }
# # for open in states:
# #     print("key is " + open)
# #     print("value is " + states[open])
# #
# for life in roberts_life:
#     print("key is " + life)
#     if type(roberts_life[life]) == type("dict"):
#         for nested_key in roberts_life[life]:
#             print("nested key is " + nested_key)
#             print("nested value is " + roberts_life[life])
#     # print("value is " + str(roberts_life[life]))
    # for movie in movies:
    #     print("key is " + movie)
    #     print("value is " + movies[movie])
