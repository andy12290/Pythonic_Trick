# will see the enumurate function
test = ['Aniket', 'Kale', 'Devidas']

# loop
for index, value in enumerate(test):
    # print(f '{index} {value}')
    print('This is index {} and value {}' .format(index, value))


# if you wanted start from the 1

for index, value in enumerate(test,1):
    print('This is index {} and value {}' .format(index, value))
