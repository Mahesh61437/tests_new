# generator

def gen_seq():
    print("first number")
    yield 1

    print("sec number")
    yield 2


def range_new(start, stop):

    while start < stop:
        yield start
        start += 1


# for i in range_new(0, 10):
#     print(i)

# g = range_new(0, 4)
# print(g.__next__())


# l = [1, 2, 3, 4]
# i = iter(l)
# # for i in l:
# #     print(i)
#
# print(next(i))
# print(next(i))


def dummy():

    l = [1, 2, 3, 4]
    yield from l
    # for i in l:
    #     yield i


d = dummy()

print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
