# abstraction
from abc import ABC, abstractmethod, ABCMeta


class A(metaclass=ABCMeta):
    @abstractmethod
    def print_hello(self):
        pass

    def say_hi(self):
        res = self.print_hello()
        if res == 1:
           print("1")



