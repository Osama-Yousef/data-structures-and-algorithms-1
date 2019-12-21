# Code Challenge 08 
Write a function called mergeLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Tests
```
test_binary_search_null - Test for empty array. 
test_binary_search_even - Test for even array.
test_binary_search_odd - Test for odd array.
test_binary_search_not_found - Test for target value not found in array.
```
## Challenge
Write a function called mergeLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.

## Approach & Efficiency
```
Set left and right bounds of array to left and right vars respectively.
Set mid_idx = (left + right) // 2. 
Compare val at mid_idx to target val.
If they're equal return mid_idx,
else if val @ mid > target, set right to mid, else set left to mid val.
Repeat until left == right. If target value not found, return -1.
```

Big O notation
```
time <- O(log n)
space <- O(log n)
```
## Solution
![whiteboard](./assets/code-challenge08)