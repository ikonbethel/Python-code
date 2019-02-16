#passing a function as a parameter using math import
#python data science programming
#created by ikon beth

from math import log

def square_input(x):
    return x*x

#defines a generic function which takes another function as input
#and applies it on given input sequence

def apply_func(func_x, input_x):
    return map(func_x, input_x)
    


a = [2,3,4,5]
b = apply_func(square_input, a)
c = apply_func(log, a)
#d = map(b,c)
#e = list(d)
print(map(b,c))
print(c)
