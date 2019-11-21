# 5行4列
# 可以额外写一个函数，判断两个点是否挨着，挨着的话直接返回

Game_Map = [['#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', ' ', '#'],
            [' ', '#', '#', '#', ' '],
            ]
all_solutions = []
points = []


def findNextPoints(point):
    x = point[0]
    y = point[1]
    near_points = findNearPoints(point)
    next_points = []
    for near_point in near_points:
        if Game_Map[near_point[0]][near_point[1]] == " " and \
                [near_point[0], near_point[1]] not in points:
            next_points.append([near_point[0], near_point[1]])
    return next_points


def findNearPoints(point):
    x = point[0]
    y = point[1]
    near_points = [[x - 1, y], [x, y - 1], [x + 1, y], [x, y + 1]]
    next_points = []
    for i in range(len(near_points)):
        if near_points[i][0] in [-1, 4]:
            if near_points[i][0] == -1:
                near_points[i][0] = 3
            else:
                near_points[i][0] = 0
        if near_points[i][1] in [-1, 5]:
            if near_points[i][1] == -1:
                near_points[i][1] = 4
            else:
                near_points[i][1] = 0
    return near_points


def near_The_Point(point1, point2):
    return point2 in findNearPoints(point1)


def Solution_findMinSteps(point1, point2, steps):
    if near_The_Point(point1, point2):
        all_solutions.append(steps)

    next_points = findNextPoints(point1)
    # print("候选空格点：")
    # print(next_points)
    for next_point in next_points:
        # 进入下一个空格点
        # print("进入空格点：")
        # print(next_point)
        steps = steps + 1
        points.append(next_point)
        Solution_findMinSteps(next_point, point2, steps)


def findMinSteps(point1, point2):
    if near_The_Point(point1, point2):
        return "这俩挨着，不用算了"
    points.clear()
    all_solutions.clear()
    steps = 0  # 走过的步数
    Solution_findMinSteps(point1, point2, steps)
    if len(all_solutions) == 0:
        return "impossible"
    else:
        return min(all_solutions)


if __name__ == '__main__':
    print("Pair 1:" + str(findMinSteps([2, 1], [3, 3])) + " segments.")  # 正确答案为4 (第三行第二列的点到第四行第四列的点需要走4个空格)
    print("Pair 1:" + str(findMinSteps([2, 0], [3, 3])) + " segments.")  # 正确答案为2 (第三行第一列的点到第四行第四列的点需要走2个空格，允许打破边界)
    print(findMinSteps([2, 1], [3, 2]))  # 正确答案为impossible （两点不存在只包含空格的路径）
    # print(findNextPoints([1, 0]))
    # print(findNearPoints([1, 0]))
