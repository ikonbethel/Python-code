#get a dictionary keys and values from the list given
#created by ikon beth

wordlist = ['apple', 'durian', 'banana', 'durian', 'apple', 'cherry', 'cherry',
            'mango', 'apple', 'apple', 'cherry', 'durian', 'banana', 'apple',
            'apple', 'apple', 'apple', 'banana', 'apple']


fruit_dict = {}
for fruit in wordlist:
    if fruit not in fruit_dict:
        fruit_dict[fruit] = 1
    else:
        fruit_dict[fruit] += 1

print(fruit_dict)

