class Solution:
    def Sum_Solution(self, n):
        # write code here
        if n == 1:
            return 1
        else:
            return n + self.Sum_Solution(n - 1)

    def jumpFloorII(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2

        sum_ = 0
        for i in range(number):
            sum_ = sum_ + self.jumpFloorII(i)
        return sum_ + 1


solut = Solution()
print(1, solut.Sum_Solution(5))
print(2, solut.jumpFloorII(10))
