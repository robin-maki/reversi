import copy

DIRECTION = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


class Game:
    def __init__(self, gameBoard=None):
        """
        Game 클래스의 생성자
        :param gameBoard?: (List[8][8]) 게임의 초기 상태 List, 주어지지 않으면 게임 초기상태로 초기화한다
        """
        if gameBoard is None:
            self.gameBoard = []
            for i in range(8):
                self.gameBoard.append([0, 0, 0, 0, 0, 0, 0, 0])
            self.gameBoard[3][3] = self.gameBoard[4][4] = -1
            self.gameBoard[3][4] = self.gameBoard[4][3] = 1
        else:
            self.gameBoard = copy.deepcopy(gameBoard)

    def checkFlippable(self, x, y, my):
        """
        주어진 위치에 돌을 놓을때 뒤집을 수 있는 돌의 위치 List를 리턴한다.
        :param x: (int) 돌을 놓을 위치의 x좌표
        :param y: (int) 돌을 놓을 위치의 y좌표
        :param my: (int) 자신의 색깔(-1/1)
        :return: (List[][2]) 뒤집을 수 있는 돌의 위치들
        """
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
        """
        게임에서 돌을 놓을 수 있는(=하나라도 뒤집을 수 있는) 위치 List를 리턴한다.
        :param my: (int) 자신의 색깔(-1/1)
        :return: (List[][2]) 놓을 수 있는 돌의 위치들
        """
        flippable = []
        for i in range(8):
            for j in range(8):
                if self.gameBoard[i][j] == 0 and len(self.checkFlippable(i, j, my)) > 0:
                    flippable.append((i, j))
        return flippable

    def place(self, x, y, my):
        """
        돌을 놓고 뒤집는다. 만약 뒤집을 수 없는 위치라면 ValueError를 일으킨다. 실제로 판을 변경한다.
        :param x: (int) 돌을 놓을 위치의 x좌표
        :param y: (int) 돌을 놓을 위치의 y좌표
        :param my: (int) 자신의 색깔(-1/1)
        :return: (List[][2]) 놓거나 뒤집은 돌들의 좌표들
        """
        toFlip = self.checkFlippable(x, y, my)
        if len(toFlip) > 0:
            toFlip.append((x, y))
            for f in toFlip:
                self.gameBoard[f[0]][f[1]] = my
            return toFlip
        else:
            raise ValueError('Invalid place')

    def getPotentialBoard(self, x, y, my):
        """
        해당 위치에 돌을 놓았을 때 결과적으로 만들어지는 gameBoard를 리턴한다. 실제로 판을 변경하지는 않는다.
        :param x: (int) 돌을 놓을 위치의 x좌표
        :param y: (int) 돌을 놓을 위치의 y좌표
        :param my: (int) 자신의 색깔(-1/1)
        :return: (List[8][8]) 해당 위치에 돌을 놓은 후의 gameBoard
        """
        potentialGame = Game(self.gameBoard)
        potentialGame.place(x, y, my)
        return potentialGame.gameBoard

    def getScore(self):
        """
        각각 돌의 갯수를 세서 리턴한다.
        :return: (List[2]) 1, -1의 돌 갯수 List
        """
        score = [0, 0]
        for i in range(8):
            for j in range(8):
                if self.gameBoard[i][j] == 1:
                    score[0] += 1
                elif self.gameBoard[i][j] == -1:
                    score[1] += 1
        return score

