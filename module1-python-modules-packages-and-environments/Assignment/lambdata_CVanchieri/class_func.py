"""
Helpers - A bit of helper code for a class function.
"""

# create a description title.
title = "A bit of helper code for a class function"


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def myfunc(text):
        print("Hi everyone my name is", text.first_name, text. last_name,  "and I am",
              text.age, "years old")


p1 = Person("Charles", "Vanchieri", 34)


p1.myfunc()
