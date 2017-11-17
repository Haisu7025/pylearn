import tensorflow as tf

with tf.name_scope("i1"):
    input1 = tf.constant([1.0, 2.0, 3.0], name="input1")
with tf.name_scope("i2"):
    input2 = tf.Variable(tf.random_uniform([3]), name="input2")
output = tf.add_n([input1, input2], name="add")

writer = tf.summary.FileWriter(
    "/Users/yhs/Github/pylearn_local/tensorflow/logs", tf.get_default_graph())
print tf.get_default_graph()
writer.close()
