# Creating a class Person and creating an inheritance using Student

name = input('What is your name?\n')
lastname = input('What is your last name?\n')

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print('Welcome to this class ' + self.firstname, self.lastname)


class Student(Person):
  pass


#Use the Person class to create an object, and then execute the printname method:

x = Student(name, lastname)
x.printname()

