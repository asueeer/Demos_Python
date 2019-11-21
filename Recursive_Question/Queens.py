import numpy

N = 16 # N皇后问题
# chess = numpy.zeros((N, N), dtype='int8')


# print(chess)
nums = 0
results = []
def findChess_choices(chess,chess_choices):
    chess_choices1 = numpy.array(chess_choices)
    for i in range(N):
        for j in range(N):
            if chess[i][j] == 1:
                chess_choices1[i, :] = 1
                chess_choices1[:, j] = 1
                for k in range(4):
                    if k == 0:
                        dx = 1
                        dy = 1
                    if k == 1:
                        dx = 1
                        dy = -1
                    if k == 2:
                        dx = -1
                        dy = 1
                    if k == 3:
                        dx = -1
                        dy = -1
                    x = i + dx
                    y = j + dy
                    while 0 <= x < N and 0 <= y < N:
                        chess_choices1[x][y] = 1
                        x = x + dx
                        y = y + dy
    return chess_choices1


def PutNextQueens(chess, chess_choices):
    newChessesAndChess_choices = []
    for i in range(N):
        if sum(chess[i]) == 1:
            pass
        else:
            for j in range(N):
                if chess_choices[i][j] == 0:
                    chess[i][j] = 1
                    newChessesAndChess_choices.append([numpy.array(chess), findChess_choices(chess,chess_choices)])
                    chess[i][j] = 0
            break
    return newChessesAndChess_choices


def Solu(chess, chess_choices):
    global nums,results
    if state(chess, chess_choices) == 'no':
        # print("no")
        return 0
    if state(chess, chess_choices) == 'yes':
        results.append(chess)
        nums = nums + 1
        return 0
    newChessesAndChess_choices = PutNextQueens(chess, chess_choices)
    for newChessAndChess_choice in newChessesAndChess_choices:
        new_chess = newChessAndChess_choice[0]
        new_chess_choices = newChessAndChess_choice[1]
        Solu(new_chess, new_chess_choices)


def state(chess, chess_choices):
    if sum(sum(chess)) == N:
        return 'yes'
    if sum(sum(chess_choices)) == N*N:
        return 'no'
    return 'possible'


if __name__ == '__main__':

    chess = numpy.zeros((N, N), dtype='int8')
    chess_choices = numpy.zeros((N, N), dtype='int8')
    Solu(chess, chess_choices)
    print(results)
    print(nums)
