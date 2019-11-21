# 熄灯问题
puzzle1 = [[0, 1, 1, 0, 1, 0],
           [1, 0, 0, 1, 1, 1],
           [0, 0, 1, 0, 0, 1],
           [1, 0, 0, 1, 0, 1],
           [0, 1, 1, 1, 0, 0]
           ]
puzzle2 = [[0, 0, 1, 0, 1, 0],
           [1, 0, 1, 0, 1, 1],
           [0, 0, 1, 0, 1, 1],
           [1, 0, 1, 1, 0, 0],
           [0, 1, 0, 1, 0, 0],
           ]


# press1 = [[1, 0, 1, 0, 0, 1],
#           [1, 1, 0, 1, 0, 1],
#           [0, 0, 1, 0, 1, 1],
#           [1, 0, 0, 1, 0, 0],
#           [0, 1, 0, 0, 0, 0]
#           ]
# press2 = [[1, 0, 0, 1, 1, 1],
#           [1, 1, 0, 0, 0, 0],
#           [0, 0, 0, 1, 0, 0],
#           [1, 1, 0, 1, 0, 1],
#           [1, 0, 1, 1, 0, 1]]


def printMatrix(Matrix):  # 按行打印二维数组
    for row in Matrix:
        print(row)
    print("")


def formatPuzzle(puzzle):
    new_puzzle = [[0 for i in range(8)] for j in range(7)]
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            new_puzzle[i + 1][j + 1] = puzzle[i][j]
    return new_puzzle


def reformatPress(press):
    new_press = [[0 for i in range(6)] for j in range(5)]
    for i in range(len(new_press)):
        for j in range(len(new_press[0])):
            new_press[i][j] = press[i + 1][j + 1]
    return new_press


def enumerateAllState(puzzle): # 核心代码
    puzzle = formatPuzzle(puzzle)
    press_all = []
    for i in range(64):
        first_press = str(bin(i)[2:])
        first_row = [0 for j in range(8)]
        for j in range(len(first_press)):
            first_row[j + 1] = int(first_press[j])
        press = calculate_Press(puzzle, first_row)
        if verify(puzzle, press):
            new_press = reformatPress(press)
            press_all.append(new_press)
    return press_all


def calculate_Press(puzzle, first_row): # 第一行按键确定，其余各行按键也应唯一确定
    press = [[0 for i in range(8)] for j in range(7)]
    press[1] = first_row
    for i in range(2, 6):
        for j in range(1, 7):
            if press[i - 1][j] ^ puzzle[i - 1][j] ^ press[i - 1][j - 1] ^ \
                    press[i - 1][j + 1] ^ press[i - 2][j] == 1:
                press[i][j] = 1
    return press


def verify(puzzle, press):
    last_row = [0 for j in range(8)]
    for j in range(1, 7):
        last_row[j] = press[5][j] ^ press[5][j - 1] ^ press[5][j + 1] ^ \
                      press[4][j] ^ puzzle[5][j]
        if last_row[j] == 1:
            return False
    return True


def stdio(puzzle):
    results = enumerateAllState(puzzle)
    if len(results) == 0:
        print("找不到合适的答案")
    else:
        for result in results:
            printMatrix(result)


if __name__ == '__main__':
    print("PUZZLE #1")
    stdio(puzzle1)
    print("PUZZLE #2")
    stdio(puzzle2)
