dictg = {1: 'one', 2: 'two'}
print(list(dictg.values()))
key = 3
print(dictg[key] if key in list(
    dictg.keys()) else 'key 3 doesn\'t exist' if key == 3 else 'No such key')
