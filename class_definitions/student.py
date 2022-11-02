"""
student.py

Author: Andrew May

Last Modified: 10/31/2022

=================================

This program defines the 'Student' class, which takes in 3 mandatory arguments

(lname, fname, major), and 1 that is optional (gpa). These inputs are tested and verified,

before finally being concatenated and printed to the screen.

(NOTE: Must be used in conjunction with test_student.py)
"""


class Student:

    def __init__(self, lname, fname, major, gpa=0.0):
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        gpa_characters = set("1234567890.")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(major)):
            raise ValueError

        if gpa and not gpa_characters.issuperset(str(gpa)):
            raise ValueError
        elif not isinstance(gpa, float):
            raise ValueError
        elif int(gpa) not in range(0, 5):
            raise ValueError

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major '" + self.major + "' with gpa: " + str(self.gpa)


if __name__ == '__main__':
    print(Student('Duck', 'Daisy', 'Communications', 3.7))
    print(Student('Duck', 'Donald', 'Marine Biology', 3.9))
