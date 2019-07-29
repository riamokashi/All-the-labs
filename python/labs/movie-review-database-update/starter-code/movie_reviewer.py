#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Using the given file movie_reviewer.py,
#Your goal is to do the following:
#
# Go to the actual IMDB site for
#Inside Out and identify which values in the
#given dictionary are inaccurate.
# Write lines of code to update the
#original dictionary with the new information.
# Remove the out_of key-value pair,
#since your boss thinks it is not needed
#since every movie is rated out of 10.
# Add the genres with the key genre and
#the value as a list of strings.
# Print out every key-value pair in the
#dictionary so you can double check that it worked.
#
#
# inside_movie = {
#     "title": "Inside Out",
#     "id": "tt2096673",
#     "year_released": 2012,
#     "rating": "PG",
#     "score": 7.5,
#     "out_of": 10,
#     "reviews": 463787
# }
# print(str(inside_movie['year_released']) + "the year release is ")
# inside_movie['year_released'] = 2015
# print( + inside_movie['year_released'])
#
# print(inside_movie)
#
# print(str(inside_movie['score']) + "the real score is ")
# inside_movie['score'] = 8.2
# print( + inside_movie['score'])
#
# print(inside_movie)
#
# print(str(inside_movie['reviews']) + "the real review is ")
# inside_movie['review'] = 541183
# print( + inside_movie['review'])
#
# print(inside_movie)

#8.2
#541183
# Do not edit the code above!

class Pokemon(object):
    def __init__(self, name, type, sex):
        self.name = name
        self.type = type
        self.sex = sex

    def attack(self):
        print("hiiiyaa")

class Pikachu(Pokemon):
    def __init__(self, name, type, sex, voltage, current):
        Pokemon.__init__(self, name, type, sex)
        self.voltage = voltage
        self.current = current


#
class Charizard(Pokemon):
    def __init__(self, name, type, sex, tail_flame_size):
        Pokemon.__init__(self, name, type, sex)
        self.tail_flame_size = tail_flame_size

charizard = Charizard("chari", "flame", "female", "large")
def burn(self):
    print("^^^^^")

charizard.attack("burn")

print("my name is " + charizard.name + " and I choose " + charizard.attack)
print(charizard.burn())
















# Write your code below to update the information in accordance with its
# IMDB page: http://www.imdb.com/title/tt209667
