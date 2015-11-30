import tensorflow as tf
import random
import os
import shutil


tensorboard_path = "/home/daniel/tensorboard_log/"
tensorboard_tmp_dir = "test1"

# delete any former tensorboard log data
if os.path.exists(tensorboard_path + tensorboard_tmp_dir):
    shutil.rmtree(tensorboard_path + tensorboard_tmp_dir)


#####################
# preparation stuff #
#####################

# define input and output data
input_data = [[0., 0.], [0., 1.], [1., 0.], [1., 1.]]  # XOR input
output_data = [0., 1., 1., 0.]  # XOR output
# input_data = [[0., 0.], [0., 0.], [0., 0.], [0., 0.]]  # XOR input
# output_data = [0., 0., 0., 0.]  # XOR output

# create a placeholder for the input
# None indicates a variable batch size for the input
# one input's dimension is [1, 2]
n_input = tf.placeholder(tf.float32, shape=[None, 2], name="n_input")

# number of neurons in the hidden layer
hidden_nodes = 5


################
# hidden layer #
################

# hidden layer's bias neuron
b_hidden = tf.Variable(0.1, name="hidden_bias")

# hidden layer's weight matrix initialized with a uniform distribution
W_hidden = tf.Variable(tf.random_uniform([2, hidden_nodes], -1.0, 1.0), name="hidden_weights")

# calc hidden layer's activation
hidden = tf.sigmoid(tf.matmul(n_input, W_hidden) + b_hidden)


################
# output layer #
################

W_output = tf.Variable(tf.random_uniform([5, 1], -1.0, 1.0), name="output_weights")  # output layer's weight matrix
output = tf.sigmoid(tf.matmul(hidden, W_output))  # calc output layer's activation


############
# learning #
############
cross_entropy = tf.nn.sigmoid_cross_entropy_with_logits(output_data, output)  # calc cross entropy between current
                                                                              # output and desired output
loss = tf.reduce_mean(cross_entropy)  # mean the cross_entropy
optimizer = tf.train.GradientDescentOptimizer(0.2)  # take a gradient descent for optimizing with a "stepsize" of 0.1
train = optimizer.minimize(loss)  # let the optimizer train


####################
# initialize graph #
####################
init = tf.initialize_all_variables()

sess = tf.Session()  # create the session and therefore the graph
sess.run(init)  # initialize all variables


# tensorboard stuff
tf.train.write_graph(sess.graph_def, tensorboard_path + tensorboard_tmp_dir, 'graph.pbtxt')

#tf.scalar_summary("Accuracy:", tf_accuracy)
tf.histogram_summary('weights_hidden', W_hidden)
tf.histogram_summary('bias hidden', b_hidden)

tf.histogram_summary('weights_output', W_output)

tf.histogram_summary('input', n_input)
tf.histogram_summary('output', output)

merged_summary_op = tf.merge_all_summaries()
summary_writer = tf.train.SummaryWriter(tensorboard_path + tensorboard_tmp_dir, sess.graph_def)

# train the network
for epoch in xrange(0, 2001):
    cvalues = sess.run([train, loss, W_hidden, b_hidden], feed_dict={n_input: input_data})  # run the training operation
    if epoch % 200 == 0:
        print("step: {:>3}".format(epoch))
        print("train: {}".format(cvalues[0]))
        print("loss: {}".format(cvalues[1]))
        print("b_hidden: {}".format(cvalues[3]))
        print("W_hidden: {}".format(cvalues[2]))
        summary_str = sess.run(merged_summary_op, feed_dict={n_input: input_data})
        summary_writer.add_summary(summary_str, epoch)

print("")
print("input: {} | output: {}".format(input_data[0], sess.run(output, feed_dict={n_input: [input_data[0]]})))
print("input: {} | output: {}".format(input_data[1], sess.run(output, feed_dict={n_input: [input_data[1]]})))
print("input: {} | output: {}".format(input_data[2], sess.run(output, feed_dict={n_input: [input_data[2]]})))
print("input: {} | output: {}".format(input_data[3], sess.run(output, feed_dict={n_input: [input_data[3]]})))