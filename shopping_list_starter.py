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

# Your program should allow for the following functionality:
# - add an item to the list
# - remove an item from the list (assume the item is already there)
# - show all items on the list (printed in a list format)
# - exit the program
#
# You should start by writing the conditionals.  Remember to use `append()` to add an item to a list and `remove()` to remove an item from a list.
#
# The program will repeatedly ask the user to choose one of the above options until the user chooses to exit the program.


choice = raw_input("add, remove, show, check, exit")
shopping_list = []

while True:
    if choice == "add":
        item = raw_input("add item")
        (shopping_list.append(item))
        print(shopping_list)
    if choice == "remove":
        item2 = raw_input("remove item")
        (shopping_list.remove(item2))
        print(shopping_list)
    elif choice == "show":
        print(shopping_list)
    elif choice == "check":
        item3 = raw_input("enter item that you want to check")
        if item3 in shopping_list:
            print("item in list")
        else:
            print("not in list")
    elif choice == "exit":
        break





    choice = raw_input("pick a letter")
