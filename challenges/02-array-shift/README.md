# Insert and shift value at middle index
Insert and shift an array in middle of given list adding new value at middle index.

## Tests

TBD

## Challenge
Write a function called insert_shift_array which takes in an array and the value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Approach & Efficiency
First we add 1 to the length of array and divide that by 2 using floor division. This gives us the index where we will insert the new value. We then use a for loop until the index == our index, insert our new value, and continue. We return the new array.

Big O notation
time <- O(n)
space <- O(n)

## Solution
![whiteboard](./assets/array-shift.jpg)