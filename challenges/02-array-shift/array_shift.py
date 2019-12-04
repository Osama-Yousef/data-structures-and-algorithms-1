def insert_shift_array(old_array, new_val):
    new_num = len(old_array + 1) // 2
    new_arr = old_array[0:new_num:]
    new_arr.append(new_val)
    new_arr.extend(old_array[new_num::])

    return new_arr