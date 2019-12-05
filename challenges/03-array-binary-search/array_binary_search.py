def binary_search(arr, target):
    left_idx = 0
    right_idx = len(arr) - 1

    if len(arr) > 1 and arr[right_idx] > target:
        while (left_idx != right_idx):
            mid_idx = ((left_idx + right_idx ) // 2)
            if target < arr[mid_idx]:
                mid_idx = right_idx 
            elif target > arr[mid_idx]:
                mid_idx = left_idx
            else:
                outcome = -1
                break
       
        if arr[mid_idx] == target:
            outcome = mid_idx
        else:
            outcome = -1
    else:
        outcome = -1

    return outcome
