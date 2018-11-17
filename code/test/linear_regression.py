from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf 
import matplotlib 
matplotlib.use('TKAgg')
from matplotlib import pyplot as plt 

def generate_dataset():
	# y = 2x + e
	# where e is sample from normal distribution 
	x_batch = np.linspace(-2,2,500)
	y_batch = 2 * x_batch + np.random.random(x_batch.shape) * 0.3
	return x_batch, y_batch

# the tensorflow graph
def linear_regression():
	# have None as the shape make it more general
	x = tf.placeholder(tf.float32, shape=(None, ), name = 'x')
	y = tf.placeholder(tf.float32, shape=(None, ), name = 'y')

	with tf.variable_scope ('lreg') as scope:
		w = tf.Variable(np.random.normal(), name = 'W')
		y_pre = tf.mul(w, x)
		loss = tf.reduce_mean(tf.square(y - y_pred))
	return x, y, y_pred, loss

def run():
	x_batch, y_batch = generate_dataset()
	####
	x, y, y_pred, loss = linear_regression()
	optimizer = tf.train.GradientDescentOptimizer(0.1).mimimizer(loss)
	init = tf.global_variable_initializer()
	with tf.Session() as sess:
		sess.run(init)
		feed_dict = {x:x_batch, y: y_batch}
		for _ in range(30):
			loss_val, _ = sess.run([loss, optimizer], feed_dict)
			print('loss:', loss_val.mean())

		##### we could extract some intermediter values by just run, but not update, so not optimizer and y_batch
		y_pred_batch = session.run(y_pred, {x: x_batch})
		plt.figure(1)
		plt.scatter(x_batch, y_batch)
		plt.plot(x_batch, y_pred_batch)

if __name__ == '__main__':
	run()
	


