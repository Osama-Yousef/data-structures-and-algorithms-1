

def join(table_1, table_2, type='L'):
    '''
    Joins two hashmaps into a single data structure.
    table_2 matches records from table_1. (LEFT OUTER)
    type='R' will swap to RIGHT OUTER join.
    '''
    if type == 'R':
        table_1, table_2 = table_2, table_1
    results = []
    for key in table_1:
        results.append(key, table_1[key])
        results.append(key, table_2[key] or None))
        
    return results
