spam = ['cats', 'dogs', 'horses', 'birds']
spam.insert(-1, 'and')
for x in range(len(spam[0:-1])):
    print spam[x] + ',',

print spam[-1]
