import time

nums = [1, 2, 3, 4, 5, 6,7,8,9,19]
t1 = time.time()
for i in range(10000):
    s = 0
    for j in nums:
        s = s + j
print(s)
t2 = time.time()
print(t2 - t1)

t1 = time.time()
for i in range(10000):
    s = 0
    for j in range(len(nums)):
        s = s + nums[j]
print(s)
t2 = time.time()
print(t2 - t1)


def sum_(A):
    if len(A) == 0:
        return 0
    else:
        return A[0] + sum_(A[1:])


if __name__ == '__main__':
    B = [1, 2, 3, 4, 5]
    t1 = time.time()
    for i in range(10000):
        sum_(B)
    t2 = time.time()
    print(t2-t1)
    print(sum_(B))