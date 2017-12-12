def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def hello():
    return "hello world!"

hello = makeitalic(makebold(hello))

print(hello())


@makeitalic
@makebold

def goodbye():
    return "I am gone!"

print(goodbye())

@makebold
@makeitalic

def good():
    return "I am good!"

print(good())
