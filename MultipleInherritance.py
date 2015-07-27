__author__ = 'varadag'

class Section(object):
    def __init__(self, name, email, **kwargs):
        self.name = name
        self.email = email

    def show(self):
        print "SHOW DETAILS"
        print "============"
        print self.name
        print self.email

if __name__ == "__main__":
    s =Section("Varadarajan","varadag@tataelxsi.co.in")