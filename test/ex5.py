# decorators
import time

def deco(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print("total time  == ", time.time() - start_time)

    return wrapper

class Counter:

    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print(self.counter)
        self.func(*args, **kwargs)

@Counter
def long_func(start, stop):
    for i in range(start, stop):
        count = 0

long_func(0, 100)
long_func(0, 1000)
long_func(0, 10000)
