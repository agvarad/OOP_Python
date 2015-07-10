__author__ = 'Python Object Oriented Programming'


class ContactDict(dict):
    def search(self, name):
        matching = []
        for data in self:
            if name in data:
                matching.append(name)
        return matching


class Contact:
    all_contacts = ContactDict()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.update({self.name:self.email})


if __name__ == "__main__":
    C = Contact('varadarajan', 'varadag@tataelxsi.co.in')
    print C.all_contacts