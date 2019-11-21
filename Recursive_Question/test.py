import numpy

from Recursive_Question.Queens import findChess_choices

chess_choices = numpy.zeros((8, 8), dtype='int8')
chess = numpy.zeros((8, 8), dtype='int8')


def PutNextQueens(chess, chess_choices):
    newChessesAndChess_choices = []
    for i in range(8):
        if sum(chess[i]) == 1:
            pass
        else:
            for j in range(8):
                if chess_choices[i][j] == 0:
                    chess[i][j] = 1
                    newChessesAndChess_choices.append([numpy.array(chess), findChess_choices(chess,chess_choices)])
                    chess[i][j] = 0
            break
    return newChessesAndChess_choices

chess[0][0]=1
chess_choices = findChess_choices(chess,chess_choices)
print(PutNextQueens(chess, chess_choices))
print(len(PutNextQueens(chess, chess_choices)))
