# Lecture 8 - OOP


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # # Getter: get attribute
    # @property
    # def house(self):
    #     return self._house

    # @property
    # def name(self):
    #     return self._name

    # # Setter: set value
    # @house.setter
    # def house(self, house):
    #     if house not in ["Vietnam", "PhuYen", "PY"]:
    #         raise ValueError("Invalid house")
    #     self._house = house

    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Missing Name")
    #     self._name = name

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")

        return cls(name, house)


def main():
    student = Student.get()
    print(student)



if __name__ == "__main__":
    main()
