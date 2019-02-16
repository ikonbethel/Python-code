#function and method overide demonstration
#created by ikon in coders apprentice
#DevCUyo100DaysOfCode

class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = int(age)
    def __repr__(self):
        return ("{} {}".format(self.firstname, self.lastname))
    def underage(self):
        if self.underage < 18:
            return self.underage

class Student(Person):
    def __init__(self, firstname, lastname, age, program):
        super().__init__(firstname, lastname, age)
        self.courselist = []
        self.program = program
    def underage(self):
        if self.underage < 21:
            return (self.underage)
    def enroll(self):
        self.courselist.append(course)


albert = Student("Albert", "Applebaum", int(19), "CSAI")
print (albert)
print(albert.underage())
print(albert.program)
albert.enroll("Method of Rationality")
albert.enroll("Defence Against the Dark Arts")
print(albert.courselist)
    
    
                
