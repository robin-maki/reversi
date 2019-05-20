import neuralnet
import game

LEARNING_COUNT = 12
WIN_COUNT = 4

learningList = []
leagueNum = 0

def init():
    for i in range(LEARNING_COUNT):
        learningList.append(neuralnet.NeuralNet())

def league():
    print('[League {}] Start!'.format(leagueNum))
    for i in range(LEARNING_COUNT):
        for j in range(i + 1, LEARNING_COUNT):
            leagueGame = game.Game()
            print('[League {}] No.{} vs No.{}'.format(leagueNum, i, j))
            while 1:
                predict1 = learningList[i].predict(leagueGame, 1)
                if predict1 is not None:
                    leagueGame.place(predict1[0], predict1[1], 1)

                predict2 = learningList[j].predict(leagueGame, -1)
                if predict2 is not None:
                    leagueGame.place(predict2[0], predict2[1], -1)

                if predict1 is None and predict2 is None:
                    score = leagueGame.getScore()
                    if score[0] > score[1]:
                        learningList[i].winScore += 1
                    elif score[0] < score[1]:
                        learningList[j].winScore += 1
                    print('[League {}] Game over! {}:{}'.format(leagueNum, score[0], score[1]))
                    for u in range(8):
                        for v in range(8):
                            if leagueGame.gameBoard[u][v] == 1:
                                print('+', end='')
                            elif leagueGame.gameBoard[u][v] == -1:
                                print('-', end='')
                            else:
                                print('0', end='')
                        print('')
                    break



init()
league()
