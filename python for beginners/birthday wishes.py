#this code shows a birthday wishes
#demonstrates keyword arguments and default parameter values
#created by ikon beth

#positional parameters
def birthday1(name, age):
    print("Happy birthday,", name ,"I hear you are ", age, " today.\n")

#parameters with default values
def birthday2(name = "Jackson", age = "1"):
    print("Happy birthday," ,name, "I hear you are ", age, "today.\n")

birthday1("Jackson", 1)
birthday1(1, "Jackson")
birthday1(name = "Jackson", age = 1)
birthday1(age = 1, name = "Jackson")

birthday2()
birthday2(name = "Catherine")
birthday2(age = 2)
birthday2(name = "Catherine", age = 12)
birthday2("Catherine", 12)
input("\nPress enter key to exit")
