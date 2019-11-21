input = [   [7],
           [3,8],
          [8,1,0],
         [2,7,4,4],
        [4,5,2,6,5]]
dp = [[0] * (len(input)) for i in range(len(input[-1]))]  #  还可以进一步用滚动数组进行空间复杂度的优化

def max_sum(input, i, j):
    n = len(input) - 1
    for x in range(n, i - 1, -1):
        for y in range(len(input[x]) - 1, j - 1, -1):
            if x == n:
                dp[x][y] = input[x][y]
            else:
                dp[x][y] = max(dp[x + 1][y + 1], dp[x + 1][y]) + input[x][y]
    return dp[i][j]

if __name__ == '__main__':
    print(max_sum(input, 0, 0))