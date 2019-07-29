// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// // See the License for the specific language governing permissions and
// // limitations under the License.
const myAlarm= (name, time) => {
  return "WAKE UP " + name + " IT IS " + time;
}
console.log(myAlarm("Ria", "6:00AM"));

const momAlarm= (time) => {
  return "Wake up mom it is " + time;
}
console.log(momAlarm("6:00AM"));

const familyAlarm= (name, time) => {
  return "WAKE UP " + name + " IT IS " + time;
}
console.log(familyAlarm("dad", "6:00am"));

const important_alarm= (message) => {
  return message.toUpperCase();
}
console.log(important_alarm("wake up, wake up, wake UP!"));

const snoozeAlarm= (numberTime) => {
  let numberTime2 = numberTime + 1
  return "the alarm for " + numberTime + " has been changed to " + numberTime2;
}
console.log(snoozeAlarm(3));

const manyPeople= (numberPeople) => {
  return "Wake up! ".repeat(numberPeople);
}
console.log(manyPeople(5));
