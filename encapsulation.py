# encapsulation

class A:

    a: int  # normal
    _c: int  # protected
    __b: int  # private

    def __init__(self, a, b, c):
        self.a = a
        self.__b = b
        self._c = c

    def print_b(self):
        print(self.__b)

    def set_b(self, b):
        self.__b = b

    def _print_c(self):
        print(self._c)
        self.__print()

    def __print(self):
        print(self._c)


class B(A):

    def func(self):
        print(self.a)
        # print(self.__b)
        print(self._c)

        super().print_b()


obj = B(10, 20, 30)

obj.func()
#
# obj.__b = 100
# obj._c = 40
# print(obj._c)
# obj.print_b()
