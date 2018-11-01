spam = ['cats', 'dogs', 'horses', 'birds']
spam.insert(-1, 'and')
spam.append(',')

# Currently breaks when ran with the spam += ',' in the for loop - don't run or have fun trying to get out

for val in spam:
    spam += ','
    print(val),
