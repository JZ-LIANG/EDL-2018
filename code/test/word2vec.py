 # framword constanst
 # 30000 batch
 batch_size = 128
 vocabulary_size = 50000
 embedding_size = 128 # dimension of vector
 num_sampled = 64 # number of negetive example to sample

 # load data
 train_data , val_data,  reverse_dictionary = load_data() #reverse_dictionary == mapping from word index to word

 def skipgram():
 	batch_inputs = tf.placeholder(tf.int32, shape = [batch_size,])
 	bacth_labels = tf.placeholder(tf.int32, shape = [batch_size,1])
 	val_dataset = tf.constanst(val_data, dtype = tf.int32)

 	with tf.variable_scope('word2vec') as scope:
 		embeddings = tf.Variable(tf.random_uniform(vocabulary_size, embedding_size))
 		batch_embeddings = tf.nn.embedding_lookup(embeddings, batch_inputs)# find embedding vector element in embeddings matrix
 		weights = tf.Variable(tf.truncated_normal([vocabulary_size, embedding_size], stddev = 1.0/math.sqrt(embedding_size)))
 		biases =tf.Variable(tf.zeros([vocabulary_size]))

 		# softmax - cross entropy loss
 		# the loss is given to multiple sample in a batch, so need to be average
 		loss = tf.reduce_mean( tf.nn.nce_loss(weights = weights,
	 								biases =biases,
	 								labels = bacth_labels,
	 								inputs = batch_inputs,
	 								num_sampled = num_sampled,
	 								num_classes = vocabulary_size))

 		norm = tf.sqrt(tf.reduce_mean(tf.square(embeddings), 1, keep_dims =True))
 		normalized_embedding = embeddings/norm


 		# valuatation
 		val_embeddings = tf.nn.embedding_lookup(normalized_embedding, val_dataset)
 		similarity = tf.matmul(val_embeddings, normalized_embedding, transpose_b = True)

 		return batch_inputs, batch_size, normalized_embedding, loss, similarity

 	def run():
 		batch_inputs, batch_size, normalized_embedding, loss, similarity = skipgram()	
		optimizer = tf.train.GradientDescentOptimizer(1.0).minimize(loss)

 		init = tf.global_variable_initializer()

 		with tf.Session() as sess:
 			sess.run(init) 
 			average_loss = 0.0
 			for step, batch_data in enumerate(train_data):
 				inputs, labels = batch_data
 				feed_dict = {batch_inputs: inputs, bacth_labels = labels}

 				_, loss_val = sess.run([optimizer, loss], feed_dict)
 				average_loss += loss_val

 				if step % 1000 ==0:
 					if step >0:
 						average_loss /= 1000
 					print ('loss at iter', step, ':', average_loss)
 					average_loss = 0

 				if step % 5000 ==0:
 					sim = similarity.eval() # == sess.run()
 					for in in xrange(len(val_data)):
 						top_k = 8
 						nearest = (sim[i,:]).argsort()[1:top_k+1]
 						print_closest_words(val_data[i], nearest, reverse_dictionary)
 			final_embeddings = normalized_embedding.eval()
