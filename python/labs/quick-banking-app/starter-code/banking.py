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

# Replace "pass" with your code

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance
    def __str__(self):
        return "the lable is " + self.label + " and your balance is " + str(self.balance)
    def withdraw(self, moneyOut):
        if moneyOut > self.balance:
            return False
        if moneyOut < 0:
            return False
        self.balance = self.balance - moneyOut
    def deposit(self, moneyIn):
        if moneyIn < 0:
            return False
        self.balance = self.balance + moneyIn
    def rename(self, newName):
        if newName == "":
            return False
        self.label = newName
