#Pickle it program
#demonstates the pickling and shelving data
#created by ikon beth


import pickle, shelve
print ("Pickling lists.")
#variety = ('"hot", "sweet", "dill"')
#shape = ('"whole", "spear", "chip"')
variety = ("This is a line 1\n")
shape = ("This carries shapes\n")
brand = ("This is a Tommy Hilfiger brand")
#brand = ('"Clausen", "Heinz", "Vlassic"')
pickle_file = open("pickles1.txt", "w")
pickle.dump(variety, pickle_file)
pickle.dump(shape, pickle_file)
pickle.dump(brand, pickle_file)
pickle_file.close()

input("Press enter key to exit")
