def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

# printPicnic() takes in a dictionary of information and uses center() / ljust() to display the information

printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
