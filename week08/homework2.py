# 自定义一个 python 函数，实现 map() 函数的功能。


def my_map(func, data):
    res = []
    for i in data:
        res.append(func(i))
    return iter(res)


if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    d1 = my_map(lambda x: x*x, data1)
    print(d1)
    print(list(d1))
    print("############################################################")

    data2 = (1, 2, 3, 4, 5)
    d2 = my_map(lambda x: x + 3, data2)
    for d in d2:
        print(d)
    print("############################################################")

    data3 = ('1', '2', '3', '4', '5')
    d3 = my_map(lambda x: x + '1', data3)
    while True:
        try:
            print(next(d3))
        except StopIteration:
            print("##########meet StopIteration!")
            break
    print("############################################################")


# output:
# <list_iterator object at 0x000002815D256B50>
# [1, 4, 9, 16, 25]
# ############################################################
# 4
# 5
# 6
# 7
# 8
# ############################################################
# 11
# 21
# 31
# 41
# 51
# ##########meet StopIteration!
# ############################################################



