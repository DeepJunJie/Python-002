# 区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
#
# list
# tuple
# str
# dict
# collections.deque

if __name__ == '__main__':
    print("扁平序列：str ")
    print("容器序列：list, tuple, dict, collections.deque")
    print("可变序列: list, dict, collections.deque")
    print("不可变序列: tuple，str")

# output:
# 扁平序列：str
# 容器序列：list, tuple, dict, collections.deque
# 可变序列: list, dict, collections.deque
# 不可变序列: tuple，str