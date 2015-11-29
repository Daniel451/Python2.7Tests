import numpy as np
import tensorflow as tf
import timeit
import time


a = np.random.rand(1000, 1000).astype(np.float32)
b = np.random.rand(1000, 1000).astype(np.float32)

print("\nNumPy dot product of 1000x1000 matrix (100 repetitions): {}s\n"
      .format(timeit.timeit("np.dot(a, b)", "from __main__ import a, b, np", number=100)))

time.sleep(1)

tfa = tf.Variable(np.copy(a).astype(np.float32))
tfb = tf.Variable(np.copy(b).astype(np.float32))

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

product = tf.matmul(a, b)

print("\nTensorFlow matmul of 1000x1000 matrix (100 repetitions): {}s\n"
      .format(timeit.timeit("sess.run(product)", "from __main__ import tfa, tfb, tf, sess, product", number=100)))