# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。

import time


def timer(func):
    def func_wrapper(*args, **kwargs):
        print("####################In func_wrapper!")
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"func：{func.__name__} cost：{duration}")
        return res
    return func_wrapper


@timer
def func1(a, b):
    print("####################func1 start!")
    res = a + b
    print(f"res：{res}")
    time.sleep(2)
    print("####################func1 end!")


@timer
def func2(*args, **kwargs):
    print("####################func2 start!")
    print(args)
    print(kwargs)
    time.sleep(1)
    print("####################func2 end!")


if __name__ == '__main__':
    func1(100, 200)
    func2(2, 3, 6, 7, name='smith')


# output:
# ####################In func_wrapper!
# ####################func1 start!
# res：300
# ####################func1 end!
# func：func1 cost：2.000398635864258
# ####################In func_wrapper!
# ####################func2 start!
# (2, 3, 6, 7)
# {'name': 'smith'}
# ####################func2 end!
# func：func2 cost：1.0003149509429932
