input = [   [7],
           [3,8],
          [8,1,0],
         [2,7,4,4],
        [4,5,2,6,5]]
dp = dict()

def max_sum(input, i, j):
    n = len(input) - 1
    for x in range(n, i - 1, -1):
        for y in range(len(input[x]) - 1, j - 1, -1):
            if x == n:
                dp[str([x,y])] = input[x][y]
            else:
                dp[str([x,y])] = max(dp[str([x + 1, y + 1])], dp[str([x + 1, y])]) + input[x][y]
    return dp[str([x,y])]

if __name__ == '__main__':
    # print(max_sum(input, 0, 0))
    a = [[0]*10 for i in range(10)]
    print(a)
    a[0] = 1
    print(a)