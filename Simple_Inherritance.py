__author__ = 'Python Object Oriented Programming'


class News:
    def __init__(self):
        self.Headlines_Today = ['India wins world cup','Threat at the Border','Big data and Hadoop and happy minds.']
        self.Headlines_Yesterday = ['India on big final','India-Pak border issue continues','What is new in computers']

    def todaysnews(self):
        for headlines in self.Headlines_Today:
            print headlines

    def yesterdaysnews(self):
        for headlines in self.Headlines_Yesterday:
            print headlines

class Hindu(News):
    pass

if __name__ == "__main__":
    H = Hindu()
    print H.todaysnews()


