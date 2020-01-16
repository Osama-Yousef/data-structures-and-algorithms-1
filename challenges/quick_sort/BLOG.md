# Blog for Code Challenge 28 - Quick Sort

## Description

Quick Sort is a sorting algorithm that works in a divide and conquer way. ...

### Pseudocode

```pseudocode
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value 
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right. 
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

### Python3 Implementation

```python3

```

## Trace

### Pass 1

![Pass 1](./assets/)

### Pass 2

![Pass 2](./assets/)

### Pass 3

![Pass 3](./assets/)

### Pass 4

![Pass 4](./assets/)

### Pass 5

![Pass 5](./assets/)
