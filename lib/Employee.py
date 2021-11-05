import abc


class Employee(abc.ABC):
    # Initializer
    def __init__(self, Id, name):
        self.name = name
        self.Id = Id

    def __repr__(self):
        return str(self.__dict__)


class Junior(Employee):
    pass


class Senior(Employee):
    pass


class Manager(Employee):
    pass


class Director(Employee):
    pass