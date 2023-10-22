# работа со списками и кортежами ---------------------------

# spisok = []
# print(type(spisok))
# spisok.append('stroka')
# spisok.append(5)
# spisok.append(('korteg', 56, True))
# print(spisok)
# print(len(spisok))
# spisok.extend(['new list', 23423, False, None])
# print(spisok)
#
# korteg = tuple(spisok)
# print(korteg)
# korteg = 1, 4, 'asdas', 3.23, True
# print(korteg)

# работа со словарями ----------------------------------------
NewDict = {2: 'qwqw', 'one': 1, 'two': 'two', 'key1': 'value1'}
print(NewDict)
NewDict2 = dict.fromkeys(['key1', 'key2', 'key3'], ['value1', 'value2', 'value3'])
print(NewDict2)
print(NewDict.items())
NewDict['key2'] = 'value2'
print(NewDict)
print('key2' in NewDict)
