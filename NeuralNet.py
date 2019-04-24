import tensorflow as tf

x = tf.placeholder(tf.float32)
#y = tf.placeholder(tf.float32)

w1 = tf.Variable(tf.random_uniform([64, 1], 0.0, 1.0))
b1 = tf.Variable(tf.zeros([64, 1]))

h = tf.matmul(tf.add(x, b1), w1)
h = tf.nn.relu(h)

sess = tf.Session()
res = sess.run(h, feed_dict={x: tf.random_uniform([64, 1], 0.0, 1.0)})
print(res)