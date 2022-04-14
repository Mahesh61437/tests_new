def min_operations(n, k, a):

    if n == k:
        print(1)
        return

    max_num = max(a)
    max_num_index = a.index(max_num)
    max_index_copy = max_num_index
    steps = 0

    if min(a) == max_num_index:
        print(0)
        return

    if ((n - 1) - max_num_index) < (k - 1):
        max_num_index = max_index_copy = (n-1)

    elif max_num_index < (k - 1):
        max_num_index = max_index_copy = 0

    while max_num_index < (n - 1):
        next_index = max_num_index + k - 1
        sub_array = a[max_num_index: next_index]
        max_num_index = next_index

        if min(sub_array) == max(sub_array):
            continue

        steps += 1

    max_num_index = max_index_copy
    while max_num_index > 0:
        next_index = max_num_index - k + 1

        if next_index < 0:
            next_index = 0

        sub_array = a[next_index: max_num_index]
        max_num_index = next_index

        if min(sub_array) == max(sub_array):
            continue

        steps += 1

    print(steps)


if __name__ == '__main__':
    n = 11  #int(input())
    k = 4  # int(input())

    a = [7, 8, 6, 10, 7, 8, 9, 1, 2, 1, 7]

    # for i in range(n):
    #     a.append(int(input()))

    min_operations(n, k, a)
