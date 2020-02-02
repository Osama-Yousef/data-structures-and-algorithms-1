# Blog for Code Challenge 28 - Quick Sort

## Description

Quick sort is similar to merge sort, in that it's a conquer and divide style sorting algorythm. It chooses a pivot value and partitions the input array into a left and right array. The main difference  between merge sort and quick sort is that by the time quick sort has broken up the array into sub arrays of single elements the array is sorted.

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
def quick_sort(arr, left_idx=None, right_idx=None):
    '''Partition the array by setting the position of the pivot value '''
    if left_idx == None and right_idx == None:
        left_idx = 0
        right_idx = len(arr) - 1
    if left_idx < right_idx:
        position = partition(arr, left_idx, right_idx)
        # sort the furthest index to the left
        quick_sort(arr, left_idx, position - 1)
        # Sort the furthest index to the right
        quick_sort(arr, position + 1, right_idx)

def partition(arr, left_idx, right_idx):
    '''The point of a pivot value is to select a value, 
    find out where it belongs in the array while moving everything lower than that value
    to the left, and everything higher to the right.'''
    # set a pivot value as a point of reference
    pivot = arr[right_idx]
    # create a variable to track the largest index of numbers lower
    # than the defined pivot
    low_idx = left_idx - 1
    for current_idx in range(left_idx, right_idx):
        if arr[current_idx] <= pivot:
            low_idx += 1
            swap(arr, current_idx, low_idx)

    swap(arr, right_idx, low_idx + 1)

    return low_idx + 1

def swap(arr, current_idx, low_idx):
    '''Helper function used to shove values lower 
    than pivot value over to the left'''
    temp = arr[current_idx]
    arr[current_idx] = arr[low_idx]
    arr[low_idx] = temp
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
