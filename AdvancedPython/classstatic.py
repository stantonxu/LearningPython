#! /usr/bin/env python3

class Methods(object):
    classVariable = "classVariable"

    def instanceMethod(self,x):
        print("Executing instanceMethod (%s,%s)" % (self, x))
        print("instanceMethod: class variable: %s" % (self.classVariable))

    @classmethod
    def classMethod(cls,x):
        print("Executing classMethod (%s, %s)" % (cls, x))
        print("classMethod: class variable: %s" % (cls.classVariable))

    @staticmethod
    def staticMethod(x):
        print("Executing staticMethod (%s)" % (x))

method = Methods()

method.instanceMethod("instanceMethod")
print("\n")
Methods.classMethod("classMethod")
print("\n")
Methods.staticMethod("staticMethod")