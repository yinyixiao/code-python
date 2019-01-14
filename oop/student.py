class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__score
    def set_score(self, score):
        self.__score = score
    def print_score(self):
        print(self.get_name(),self.get_age())
bart = Student('Bart Simpson', 59)
bart.set_score(11)
print(bart.get_age())