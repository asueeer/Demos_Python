# 8行8列
from Enumeration_Question.CloseLight import printMatrix

ChessMap = [[1, 1, 1, 1, 1, 1, 1, 3],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 0, 3]]

Dictionary = dict()


def sigma(new_ChessMap):
    numbers = []
    for row in new_ChessMap:
        for index in row:
            numbers.append(index)
    # mean = sum(numbers) / len(numbers)
    # numbers_2 = []
    # for i in numbers:
    #     numbers_2.append(i * i)
    # var = sum(numbers_2) - len(numbers) * mean * mean
    # return pow(var / len(numbers), 1 / 2)
    return sum(numbers) * sum(numbers)


def func(x1, y1, x2, y2):
    new_ChessMap = []
    temp = ChessMap[x1:x2 + 1]
    for row in temp:
        new_ChessMap.append(row[y1:y2 + 1])
    return sigma(new_ChessMap)


def FindMinWayToDivide(n, x1, y1, x2, y2):
    s = str([n, x1, y1, x2, y2])
    if s in Dictionary.keys():
        return Dictionary[s]

    if n == 1:
        Dictionary[s] = func(x1, y1, x2, y2)
        return Dictionary[s]

    results = []
    for i in range(x1, x2):
        results.append(FindMinWayToDivide(n - 1, x1, y1, i, y2) + FindMinWayToDivide(1, i + 1, y1, x2, y2))
        results.append(FindMinWayToDivide(1, x1, y1, i, y2) + FindMinWayToDivide(n - 1, i + 1, y1, x2, y2))
    for i in range(y1, y2):
        results.append(FindMinWayToDivide(n - 1, x1, y1, x2, i) + FindMinWayToDivide(1, x1, i + 1, x2, y2))
        results.append(FindMinWayToDivide(1, x1, y1, x2, i) + FindMinWayToDivide(n - 1, x1, i + 1, x2, y2))
    Dictionary[s] = min(results)
    return Dictionary[s]


if __name__ == '__main__':
    score = pow((3 * FindMinWayToDivide(3, 0, 0, 7, 7) - func(0, 0, 7, 7)) / 9, 1 / 2)
    print(score)
    # 正确结果为 1.633

    # for item in Dictionary:
    #     print(str(item) + " " + str(Dictionary[item]))
    # print(Dictionary)


