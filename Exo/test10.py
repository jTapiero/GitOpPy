import test9
from test11 import yo

def test():
    test9.yo=60
test()
print(test9.yo)

def test2():
    global yo
    yo=65
test2()
print(yo)