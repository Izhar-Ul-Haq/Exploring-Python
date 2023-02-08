import tensorflow as tf
# Constants creation for TensorBoard visualization
a = tf.constant(10,name="a")
b = tf.constant(90,name="b")
y = tf.Variable(a+b*2,name='y')
model = tf.compat.v1.global_variables_initializer()
 #Creation of model
with tf.compat.v1.Session() as session:
 merged = tf.summary.merge(model)
 writer = tf.train.SummaryWriter("/tmp/tensorflowlogs",session.graph)
 session.run(model)
 print(session.run(y))

# Pass for now