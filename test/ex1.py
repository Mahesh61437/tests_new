
def result(A, N, B):
    help = 1
    s = 0
    c = 1
    a = A

    if A < N:
        return -1

    while c <= B:

        if c == 6 and s < N:
            return -1
        elif A <= 0 and c != 6:
            help += 1
            A = a

        s += (A - N)

        c += 1
        A -= N

    return help


if __name__ == '__main__':
    A = int(input())
    N = int(input())
    B = int(input())

    print(result(A, N, B))
