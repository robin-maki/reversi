import copy

DIRECTION = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


class Game:
    def __init__(self, gameBoard=None):
        if gameBoard is None:
            self.gameBoard = []
            for i in range(8):
                self.gameBoard.append([0, 0, 0, 0, 0, 0, 0, 0])
            self.gameBoard[3][3] = self.gameBoard[4][4] = 1
            self.gameBoard[3][4] = self.gameBoard[4][3] = -1
        else:
            self.gameBoard = copy.deepcopy(gameBoard)

    def checkFlippable(self, x, y, my):
        if self.gameBoard[x][y] != 0:
            return []
        flippable = []
        for d in DIRECTION:
            tx = x
            ty = y
            possible = []
            while 1:
                tx += d[0]
                ty += d[1]
                if (not (0 <= tx <= 7 and 0 <= ty <= 7)) or self.gameBoard[tx][ty] == 0:
                    break
                if self.gameBoard[tx][ty] == my:
                    flippable.extend(possible)
                    break
                else:
                    possible.append((tx, ty))
        return flippable

    def getPlaceable(self, my):
        flippable = []
        for i in range(8):
            for j in range(8):
                if self.gameBoard[i][j] == 0 and len(self.checkFlippable(i, j, my)) > 0:
                    flippable.append((i, j))
        return flippable

    def place(self, x, y, my):
        toFlip = self.checkFlippable(x, y, my)
        if len(toFlip) > 0:
            for f in toFlip:
                self.gameBoard[f[0]][f[1]] = my
            self.gameBoard[x][y] = my
            return toFlip
        else:
            raise ValueError('Invalid place')

    def getPotentialBoard(self, x, y, my):
        potentialGame = Game(self.gameBoard)
        potentialGame.place(x, y, my)
        return potentialGame.gameBoard

