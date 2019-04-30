DIRECTION = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

class Game:
    def __init__(self):
        self.gameBoard = []
        for i in range(8):
            self.gameBoard.append([0, 0, 0, 0, 0, 0, 0, 0])
        self.gameBoard[3][3] = self.gameBoard[4][4] = 1
        self.gameBoard[3][4] = self.gameBoard[4][3] = -1

    def checkFlippable(self, x, y, my):
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


g = Game()
print(g.checkFlippable(2, 3, -1))
