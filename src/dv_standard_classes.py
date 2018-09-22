'''
Created on Sep 21, 2018

Classes meant to be used throughout the program

@author: edgarcolin
'''

# From https://utcc.utoronto.ca/~cks/space/blog/python/EmulatingStructsInPython

# Emulating a C type structure in python.

# class MyStruct:
#   pass
# 
# ms = MyStruct()
# ms.foo = 10
# ms.bar = "abc"

# To make it briefly more complete:

class Struct:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class PYStruct(Struct):
    pass
    



