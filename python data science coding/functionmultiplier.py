# this creates an input and uses it in a function
#python data science
#created by ikon beth





class multiplier(object):
    def __init__(self, num):
        self.num = num

    def __mult__(self):
        return num

    def table(self,num):
        for i in range(1,13):
            m = i * num
            print(i," X ", num, " = ", m)
num = int(input("Type in your number to create a time table:"))
ma = multiplier(num)
ma.table(num)
#print(i," X ", num, " = ", m)
    
