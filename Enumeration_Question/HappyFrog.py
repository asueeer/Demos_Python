# 算法题：讨厌的青蛙
# 6 行 7 列
plants_ = [[2, 1],
           [6, 6],
           [4, 2],
           [2, 5],
           [2, 6],
           [2, 7],
           [3, 4],
           [6, 1],
           [6, 2],
           [2, 3],
           [6, 3],
           [6, 4],
           [6, 5],
           [6, 7]]  # 正确答案为7


# [[2, 1], [6, 6], [4, 2], [2, 5], [2, 6], [2, 7], [3, 4], [6, 1], [6, 2], [2, 3], [6, 3], [6, 4], [6, 5], [6, 7]]


def FindThatFrog(plants, rows, cols):
    # print(plants)
    max_steps = 0
    for plant1 in plants:
        for plant2 in plants:
            x1 = plant1[0]
            x2 = plant2[0]
            y1 = plant1[1]
            y2 = plant2[1]
            # print([x1,y1])
            # print([x2,y2])
            # print("")
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            if [x1, y1] == [6, 1] and [x2, y2] == [6, 2]:
                print("bingo")
                print("1 st:" + str([x1, y1]))
                print("2 nd:" + str([x2, y2]))
                x_n = x2 + dx
                y_n = y2 + dy
                while isInScope(x_n, y_n, rows, cols):
                    print("Next Point：" + str([x_n, y_n]))
                    x_n = x_n + dx
                    y_n = y_n + dy
            if isInScope(x1 - dx, y1 - dy, rows, cols) is False and isInScope(x2 + dx, y2 + dy, rows, cols):
                # print("1 st:" + str([x1, y1]))
                # print("2 nd:" + str([x2, y2]))
                # print("第max_steps点" + str([x1 + dx * max_steps, y1 + dy * max_steps]))
                if isInScope(x1 + dx * max_steps, y1 + dy * max_steps, rows, cols):
                    x_n = x2 + dx
                    y_n = y2 + dy
                    flag = 1  # 预设这是一条合法路径
                    steps = 2
                    while isInScope(x_n, y_n, rows, cols):
                        # print("下一点：" + str([x_n, y_n]))
                        if [x_n, y_n] not in plants:  # 路径不合法，将flag置0
                            # print("该路径不合法")
                            flag = 0
                        x_n = x_n + dx
                        y_n = y_n + dy
                        steps = steps + 1
                    if flag == 1:
                        max_steps = steps
                else:
                    # print("")
                    continue # 一开始写成了break，于是输出的结果就一直是3，最后debug了好久才找出来，遇到break和continue的时候，一定需要小心仔细
                # print(max_steps)
                # print("")
            else:
                pass
    return max_steps


def isInScope(x, y, rows, cols):
    if 1 <= x <= rows and 1 <= y <= cols:
        return True
    else:
        return False


if __name__ == '__main__':
    print(FindThatFrog(plants_, 6, 7))
    # for i in plants_:
    #     print(i)

