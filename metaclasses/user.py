# user.py

from library import Base

# assert hasattr(Base, 'foo'), "you broke it"

'''
class Derived(Base):
    def bar(self):
        return self.foo()
'''

class Derived(Base):
    def bar(self):
        return 'bar'

d = Derived()
print(d.bar())