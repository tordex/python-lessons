class MyClass:
    """
    Class description
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "MyClass[{}]".format(self.value)

    def func1(self):
        """
        Function description

        :return: None
        """
        print("Hello from func1 with value {}".format(self.value))

    @staticmethod
    def func2():
        print("Hello from func2")


class MySubClass(MyClass):

    def __init__(self, value1, value2):
        super().__init__(value1)
        self.value2 = value2
        print("Hello from MySubClass constructor")

    def func1(self):
        print("Hello from MySubClass::func1 with value {}".format(self.value2))
        super(MySubClass, self).func1()


if __name__ == '__main__':
    inst = MyClass(10)
    print(inst)
    inst = MyClass("Some string")
    print(inst)
    # Вызов статической функции
    MyClass.func2()

    inst = MySubClass(11, "hello")
    print(inst)
    inst.func1()

    MySubClass(666, "hello")
