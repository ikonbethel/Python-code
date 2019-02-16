#global reach program
#demonstrating global variables
#by ikonne bethel
def read_global():
    print ("From inside the local namespace of read_global(), value is:", value)

def shadow_global():
    value = "-10"
    print(" From inside the local namespace of shadow_global(), value is:", value)

def change_global():
    """global_value"""
    value = "-10"
    print("From the local namespace of change_global(), value is:", value)

#main
#value is a global variable because we're in the global namespace here
value = "10"
print("In the global namespace, value has been set to:", value, "\n")

read_global()
print("back in the global namespace, value is still:", value, "\n")

shadow_global()
print("Back in the global namespace, value is still:", value, "\n")

change_global()
print("Back in the global namespace, value has now changed to:", value, "\n")

input("Press enter key to exit:")
    
