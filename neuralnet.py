import random
import tensorflow as tf
import game

x = tf.placeholder(tf.float32, [None, 8, 8])
w = tf.placeholder(tf.float32, [64])

h = tf.reshape(
    tf.matmul(
        tf.reshape(x, [-1, 64]),
        tf.reshape(w, [64, 1])),
    [-1]
)
sess = tf.Session()
sess.run(tf.global_variables_initializer())

def run(gameBoard, weight):
    tensor = []
    for i in gameBoard:
        tensor.extend(i)
    res = sess.run(h, feed_dict={x: gameBoard, w: weight})
    return list(res)

class NeuralNet:
    def __init__(self, weight=None):
        """
        NeuralNet 클래스의 생성자
        :param weight?: (List[64]) 생성될 NeuralNet 인스턴스의 가중치값. 입력하지 않으면 무작위로 생성된다.
        """
        if weight is None:
            self.weight = []
            for i in range(64):
                self.weight.append(random.random())
        else:
            self.weight = weight[:]

    def predict(self, game, my):
        """
        자신의 가중치를 기반으로 신경망이 놓을 자리를 리턴한다.
        :param game: (Game) 현재 진행중인 게임
        :param my: (int) AI 자신의 색깔 (1/-1)
        :return: (List[2]) AI가 선택한 돌을 놓을 위치 List [x, y]
        """
        placeable = game.getPlaceable(my)
        if len(placeable) == 0:
            return None
        potencialBoard = []
        for potencial in placeable:
            potencialBoard.append(game.getPotentialBoard(potencial[0], potencial[1], my))
        value = run(potencialBoard, self.weight)
        if my == 1:
            most = value.index(max(value))
        else:
            most = value.index(min(value))
        return placeable[most]


n = NeuralNet()
g = game.Game()
print(n.predict(g, 1))
