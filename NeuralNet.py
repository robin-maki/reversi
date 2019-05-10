import tensorflow as tf

x = tf.placeholder(tf.float32, [None, 8, 8])
y = tf.reshape(x, [-1, 64])

w = tf.Variable(tf.random_uniform([64, 1], 0.0, 1.0))

h = tf.matmul(y, w)


def run(gameBoard):
    tensor = []
    for i in gameBoard:
        tensor.extend(i)
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    res = sess.run(h, feed_dict={x: [gameBoard]})
    return res


print(run([[0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, -1, 0, 0, 0],
     [0, 0, 0, -1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]]))
