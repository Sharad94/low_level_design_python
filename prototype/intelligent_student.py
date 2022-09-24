from student import Student

class IntelligentStudent(Student):
    def __init__(self, otherIntelligentStudent=None,  name=None,
                 age=None, batch=None, iq=None):
        """
        Normal constructor + Copy constructor

        :param otherIntelligentStudent: Intelligent Student object to be copied
        :param name: Name in string
        :param age: Age in int
        :param batch: Batch in string
        :param iq: Iq in int
        """
        super().__init__(otherIntelligentStudent, name, age, batch)
        self.__iq = None
        if otherIntelligentStudent is not None:
            self.__iq = otherIntelligentStudent.__iq

        if iq is not None:
            self.__iq = iq

    def __str__(self):
        # Get string representation of student part from student class
        str_rep = ("Student: [{0}], IQ: {1}".
                   format(Student(self), self.__iq))

        return str_rep

    def copy(self):
        """
        :return: IntelligentStudent object
        """
        return IntelligentStudent(self)


