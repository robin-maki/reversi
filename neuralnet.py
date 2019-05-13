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


def run(gameBoard, weight):
    tensor = []
    for i in gameBoard:
        tensor.extend(i)
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    res = sess.run(h, feed_dict={x: gameBoard, w: weight})
    return list(res)

class NeuralNet:
    def __init__(self, weight=None):
        if weight is None:
            self.weight = []
            for i in range(64):
                self.weight.append(random.random())
        else:
            self.weight = weight[:]

    def predict(self, game, my):
        placeable = game.getPlaceable(my)
        potencialBoard = []
        for potencial in placeable:
            potencialBoard.append(game.getPotentialBoard(potencial[0], potencial[1], my))
        value = run(potencialBoard, self.weight)
        if my == 1:
            most = value.index(max(value))
        else:
            most = value.index(min(value))
        print(value)
        return most


n = NeuralNet()
g = game.Game()
print(n.predict(g, 1))
