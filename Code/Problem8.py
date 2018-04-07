import random
import time


class Parent:
    attr1=''
    attr2=''
    attr3=''

    def __init__(self):

        self.attr1 = 'val1'
        self.attr2 = 'val2'
        self.attr3 = 'val3'

    def displayattributes(self):
        for row in [x for x in self.__dict__.items().__iter__()]:
            print("{0} : {1}".format( row[0], row[1]))


class Child (Parent):
    attr4 = 'val4'
    attr5 = 'val5'
    attr6 = 'val6'

    def __init__(self):

        self.attr4 = 'val4'
        self.attr5 = 'val5'
        self.attr6 = 'val6'
        Parent.__init__(self)


class Problem8:

    def problem8(self):
        child = Child()
        child.displayattributes()




# problem8 = Problem8 ()
# problem8.problem8()