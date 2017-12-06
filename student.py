from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name

        self.modules = []

        self.grades = {}

    def add_module(self,module):
        self.modules.append(module.title)
        self.grades[module.title] = module.get_grade()

    def get_list_modules(self):
        print("Modules of Student: {0:s}".format(self.name))
        for element in self.modules:
            print("\t", element)

    def get_grades(self):
        print("Grades of Student: {0:s}".format(self.name))
        for grade in self.grades:
            print("\t{0:s}: %.2f".format(grade) % self.grades[grade])


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
# me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

# me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
