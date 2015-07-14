__author__ = 'Python Object Oriented Programming'


class Contacts(object):
    """
    Gather all contact information like phone book
    """
    def __init__(self, name, email):
        """
        :param : name
        :type : string
        :param : email
        :email : email
        """
        self.name = name
        self.email = email


class Friends(Contacts):
    """
    Simple Inheritance from Contacts class
    :param : name
    :type : string
    :param : email
    :type : email
    :param : standard
    :type : string
    """
    def __init__(self, name, email, standard):
        super(Friends, self).__init__(name, email)
        self.standard = standard


if __name__ == "__main__":
    A = Friends('Prashanth', 'prashantha@tataelxsi.co.in', 'TataElxsi')
    B = Friends('Arul', 'arulprakashT@cognizant.com', 'Cognizant Technology Solutions')
    print A.name, "-----", B.name
