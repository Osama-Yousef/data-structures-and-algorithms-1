# Code Challenge 32 - Tree Intersection

| | |
|:-|:-|
| *Author:*      | Aaron Imbrock |
| *Create Date:* | 01/22/2020    |
| *Language:*    | Python 3.8    |

Given two Binary Search Trees, find common nodes in them.

## Challenge

- Write a function called tree_intersection that takes two binary tree parameters.
- Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees.

Input:

            left_tree              right_tree
            
            [A]                      [B]
           / | \                    / | \
         [B][C][D]                [E][F][G]
        / | \   | \
      [E][F][G][H][I]

Output (as set):

    (B, E, F, G)

## Approach & Efficiency 

## Tests

| Test Name     | Description       |
| :-------------|:-------------     |
| test_null_tree | Returns an empty set if either tree is null (empty) |
| test_intersection | Test that given two BTs only elements found in both sets are returned. |

## Big O notation

- time <- O(n)
- space <- O(n)

## Solution

![whiteboard](./assets/update.png)