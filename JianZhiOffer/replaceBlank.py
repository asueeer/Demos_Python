# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        lst = []
        for i in range(n + 1):
            lst.append(0)
        return self.Fibonacci1(n, lst)

    def Fibonacci1(self, n, lst):
        if n == 0:
            return 0
        if n < 3:
            return 1
        if lst[n] != 0:
            return lst[n]

        lst[n] = self.Fibonacci1(n - 1, lst) + self.Fibonacci1(n - 2, lst)
        return lst[n]


if __name__ == '__main__':
    so = Solution()
    so.replaceSpace1()
