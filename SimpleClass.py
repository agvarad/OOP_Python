__author__ = 'varad'

class PrintHello(object):
    def __init__(self,Name = None):
        self.name = Name

    def _Greet(self):
        print "Good Morning:" + self.name + "Have a nice day...."

if __name__ == "__main__":
    p = PrintHello('Varadarajan A G')
    p._Greet()