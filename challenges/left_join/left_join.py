

def join(table_1, table_2, type='L'):
    '''
    Joins two hashmaps into a single data structure.
    table_2 matches records from table_1. (LEFT OUTER)
    type='R' will swap to RIGHT OUTER join.
    '''
    if type == 'R':
        table_1, table_2 = table_2, table_1
    results = []
    for key, value in table_1.items():
        results.append([key, value, table_2.get(key, None)])
        
    return results
