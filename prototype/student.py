class Student:

    def __init__(self, otherStudent=None,  name=None,
                 age=None, batch=None):
        """
        Normal constructor + Copy constructor

        :param otherStudent: Student object to be copied
        :param name: Name in string
        :param age: Age in int
        :param batch: Batch in string
        """
        self.__name = None
        self.__age = None
        self.__batch = None
        if otherStudent is not None:
            self.__name = otherStudent.__name
            self.__age = otherStudent.__age
            self.__batch = otherStudent.__batch

        if name is not None:
            self.__name = name

        if age is not None:
            self.__age = age

        if batch is not None:
            self.__batch = batch

    def __str__(self):
        str_rep = ("Name: {0}, Age: {1}, Batch: {2}".
                   format(self.__name, self.__age, self.__batch))
        return str_rep

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_batch(self):
        return self.__batch

    def set_batch(self, batch):
        self.__batch = batch

    def copy(self):
        """
        :return: Student object
        """
        return Student(self)



