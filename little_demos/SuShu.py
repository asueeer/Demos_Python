# 求1000以内的所有素数
# if __name__ == '__main__':
#     list_ = []
#     for i in range(1, 10):
#         list2 = []
#         for j in range(1, i+1):
#             if i % j ==0:
#                 list2.append(j)
#
#         if len(list2) == 2:
#             list_.append(i)
#         else:
#             pass
#     print(list_)

# 判断一个数是不是素数
def f(x):
    for i in range(2, int(x/2)):
        if x % i == 0:
            return False

    return True


if __name__ == '__main__':
    N = 1
    for i in range(1, 1000, 2): # start =1,end =1000, step=2
        N = N + 1
        if f(i) == True:
            print(i)
    print()
    print(N)