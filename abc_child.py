from abstraction import A


class B(A):
    def _protected_func(self):
        pass

    def print_hello(self):
        pass


obj = B()
obj.print_hello()
