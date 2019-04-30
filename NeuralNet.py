import tensorflow as tf

x = tf.placeholder(tf.float32, [1, 64])

w = tf.Variable(tf.random_uniform([64, 1], 0.0, 1.0))

h = tf.matmul(x, w)


def run(gameBoard):
    tensor = []
    for i in gameBoard:
        tensor.extend(i)
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    res = sess.run(h, feed_dict={x: [tensor]})
    return res[0][0]


print(run([[0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, -1, 0, 0, 0],
     [0, 0, 0, -1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]]))
