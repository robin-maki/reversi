import neuralnet
import game
import json

LEARNING_COUNT = 12  # 한번에 학습할 신경망의 수
WIN_COUNT = 4   # 한 게임에 살아남는 신경망의 수

assert WIN_COUNT * (WIN_COUNT - 1) / 2 <= LEARNING_COUNT, '생존 신경망이 너무 많다!!'
# 생존 신경망의 자손만으로 신경망 최대 수를 넘을 수 있다면 에러를 발생시킴

learningList = []
leagueNum = 0


def init():
    """
    이미 학습된 데이터가 있다면 불러오고 없으면 새로운 학습 데이터를 만든다.
    """
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
    """
    지금까지의 학습 데이터를 파일에 저장한다.
    """
    with open('learn.json', 'w') as jsonFile:
        weights = []
        for l in learningList:
            weights.append(l.weight)
        jsonFile.write(json.dumps(weights))
        jsonFile.close()


def load():
    """
    파일에 저장된 학습 데이터를 불러온다.
    """
    with open('learn.json', 'r') as jsonFile:
        global learningList
        loadList = []
        for w in json.load(jsonFile):
            loadList.append(neuralnet.NeuralNet(w))
        learningList = loadList
        jsonFile.close()


def league():
    """
    현재 존재하는 신경망들끼리 리그 게임을 진행한 후,
    승률이 높은 신경망들만 살리고 각각 신경망들의 자손을 만든다.
    남은 자리는 다시 랜덤 신경망으로 채운다.
    """
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
