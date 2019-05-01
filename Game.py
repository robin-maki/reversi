import blockclass as bc
DIRECTION = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


       
def checkFlippable(x, y, my):
    if bc.board[x][y].blockstate != 0:
        return []
    flippable = []
    for d in DIRECTION:
        tx = x
        ty = y
        possible = []
        while 1:
            tx += d[0]
            ty += d[1]
            if (not (0 <= tx <= 7 and 0 <= ty <= 7)) or bc.board[tx][ty].blockstate == 0:
                break
            if bc.board[tx][ty].blockstate == my:
                flippable.extend(possible)
                break
            else:
                possible.append((tx, ty))
    return flippable

def getPlaceable(my):
    flippable = []
    for i in range(8):
        for j in range(8):
            if bc.board[i][j].blockstate == 0 and len(checkFlippable(i, j, my)) > 0:
                flippable.append((i, j))
    return flippable

def place(x, y, my):
    toFlip = checkFlippable(x, y, my)
    if len(toFlip) > 0:
        bc.board[x][y].blockstate = my
        for f in toFlip:
            bc.board[f[0]][f[1]].blockstate = my
        return toFlip
    else:
        raise ValueError('Invalid place')
