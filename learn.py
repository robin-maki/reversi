import neuralnet
import game
import json

LEARNING_COUNT = 12
WIN_COUNT = 4

assert WIN_COUNT * (WIN_COUNT - 1) / 2 <= LEARNING_COUNT, '생존 신경망이 너무 많다!!'

learningList = []
leagueNum = 0

def init():
    from pathlib import Path
    if Path('learn.json').is_file():
        print('File exists')
        load()
    else:
        print('File not exists. Initializing')
        for i in range(LEARNING_COUNT):
            learningList.append(neuralnet.NeuralNet())
        save()

def save():
    with open('learn.json', 'w') as jsonFile:
        weights = []
        for l in learningList:
            weights.append(l.weight)
        jsonFile.write(json.dumps(weights))
        jsonFile.close()

def load():
    with open('learn.json', 'r') as jsonFile:
        global learningList
        loadList = []
        for w in json.load(jsonFile):
            loadList.append(neuralnet.NeuralNet(w))
        learningList = loadList
        jsonFile.close()

def league():
    global learningList, leagueNum
    leagueNum += 1
    winlose = 0
    print('[League {}] Start!'.format(leagueNum))
    for i in range(LEARNING_COUNT):
        learningList[i].winScore = 0
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
                        learningList[i].winScore += (score[0] - score[1])
                    elif score[0] < score[1]:
                        learningList[j].winScore += (score[1] - score[0])
                    print('[League {}] Game over! {}:{}'.format(leagueNum, score[0], score[1]))
                    '''
                    for u in range(8):
                        for v in range(8):
                            if leagueGame.gameBoard[u][v] == 1:
                                print('+', end='')
                            elif leagueGame.gameBoard[u][v] == -1:
                                print('-', end='')
                            else:
                                print('0', end='')
                        print('')
                    '''
                    if score[0] > score[1]:
                        winlose += 1
                    elif score[0] < score[1]:
                        winlose -= 1
                    break
    print('[League {}] W/L Point: {}'.format(leagueNum, winlose))
    learningList.sort(key=lambda nn: nn.winScore, reverse=True)
    newLearningList = []
    for i in range(WIN_COUNT):
        for j in range(i + 1, WIN_COUNT):
            newLearningList.append(learningList[i].gen(learningList[j]))
    while len(newLearningList) < LEARNING_COUNT:
        newLearningList.append(neuralnet.NeuralNet())
    learningList = newLearningList
    save()
