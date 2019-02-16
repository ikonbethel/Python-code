# this converts a text strings to dictionary item
#created by ikon beth
#DevCUyo100DaysOfCode
import pprint
text = " apple, durian, banana, durian, apple, cherry, cherry, mango," + \
       " apple, apple, cherry, durian, banana, apple, apple, apple,"  + \
       " apple, banana, apple"
fruitlist = text.split(',')
fruit_dict ={}
for fruit in fruitlist:
    if fruit not in fruit_dict:
        fruit_dict[fruit] = 1
    else:
        fruit_dict[fruit] += 1

pprint.pprint (fruit_dict)
