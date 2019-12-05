def binary_search(arr, target):
    left_idx = 0
    right_idx = len(arr) - 1
    outcome = -1

    if arr != []:
        while (left_idx != right_idx) and (outcome != -1):
            mid_idx = ((left_idx + right_idx ) // 2)
            if target < arr[mid_idx]:
                mid_idx = right_idx 
            elif target > arr[mid_idx]:
                mid_idx = left_idx
            else:
                break
        
        
            if arr[mid_idx] == target:
                outcome = mid_idx
            else:
                outcome = -1

    return outcome
