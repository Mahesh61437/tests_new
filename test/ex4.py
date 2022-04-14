#logic

if __name__ == '__main__':
    n = 3  # int(input())

    ary = [[5, 10], [3, 7], [1, 2]]
    # for i in range(n):
    #     ary.append(list(map(int, input().split(","))))

    # print(ary)

    gap = 1  # int(input())

    sum = 0

    for sub_arry in ary:
        sum += sub_arry[-1] - sub_arry[0]

    print(sum + (n-1) * gap)
