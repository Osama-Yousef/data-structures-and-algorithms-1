# Blog for Code Challenge 26 - Insertion Sort

## Description

Selection Sort is a sorting algorithm in the same family as bubble sort and selection sort but simpler and more efficient. Selection sort works by iterating across the array starting at the front and comparing if the value of the element next to it is lower. If the next door value is lower the elements change places.

### Pseudocode

```pseudocode
SelectionSort(int []arr)
    DECLARE n <-- arr.Length;
    FOR i = 0; i to n - 1  
        DECLARE min <-- i;
        FOR j = i + 1 to n
            if (arr[j] < arr[min])
                min <-- j;

        DECLARE temp <-- arr[min]; 
        arr[min] <-- arr[i]; 
        arr[i] <-- temp;
```

### Python3 Implementation

```python3
def insertion_sort(array):
    for i in range(len(array)):
        j = i - 1
        temp = array[i]

        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = temp
```

## Trace

### Pass 1

![Pass 1](./assets/1stpass.jpg)

In the first pass we assign the value at array[1], the 2nd cell, and assign it to variable temp. We compare the value of array[0] which is 20 to the value of variable temp, which is 18. Since 20 is greater than 18 we shift the 20 to the right.

### Pass 2

![Pass 2](./assets/2ndpass.jpg)

In the second pass we remove the value at index 2 and store it in temp. temp = 12. We compare 12 to [1] 20, it's lower, and we then compare it to [0], 18, and it's also lower. temp value is assigned to [0].

### Pass 3

![Pass 3](./assets/3rdpass.jpg)

Here we assign the value of 8 to temp, compare it to 20, and because 8 is a lower value it shifts down all the way to index of 0.

### Pass 4

![Pass 4](./assets/4thpass.jpg)

In the fourth pass we assign 5 to the variable temp, comparing it to the value in the previous index, 20. Since 5 is less than 20, as well as all the others, it slides down to index of 0.

### Pass 5

![Pass 5](./assets/5thpass.jpg)

In this final pass we assign the value -2 to the variable temp, comparing it to the value in the previous element, 20. Since -2 is lower than all the previous values, it is assigned to index of 0.