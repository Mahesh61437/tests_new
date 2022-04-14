def value_of_splitting(n, a):
    sub_array = []
    pre_value = 0
    sum = 0

    for item in a:
        if pre_value <= item:
            sub_array.append(item)
        else:
            sum += (sub_array[-1] - sub_array[0])
            sub_array = [item]

        pre_value = item

    print(sum + (sub_array[-1] - sub_array[0]))


if __name__ == '__main__':
    n = 5
    a = [6, 10, 9, 2, 3]
    value_of_splitting(n, a)
