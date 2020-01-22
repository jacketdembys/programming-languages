# 1. join a string with a seperator
print('1. join a string with a seperator')
string = 'Here'
delimitor = '|'
print(delimitor.join(string))


# 2. justification
print('\n2. justification')
myString = 'Jacket&Peggy'
print(myString.rjust(20))
print(myString.rjust(20, ':'))
print(myString.ljust(20, ':'))

# join strings
print('\n3. join strings')
content = []
content.append('Jacket')
content.append('loves')
content.append('Peggy')
contentstr = ' '.join(content)
print(contentstr)

strList = []
strList.append('Line #1')
strList.append('Line #2')
strList.append('Line #3')
strListAppended = '\n'.join(strList)
print(strListAppended)