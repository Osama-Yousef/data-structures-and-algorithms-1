def insertion_sort(array):
    '''Remove, compare, shift, and insert based sort array'''
    for index in range(len(array)):
        position = index - 1
        temp = array[index]

        while position >= 0 and temp < array[position]:
            array[position + 1] = array[position]
            position = position - 1

        array[position + 1] = temp

    return array