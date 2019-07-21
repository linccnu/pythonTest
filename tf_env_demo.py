"""
The file is used to test tensorflow docker image.
Data:2019/07/21
Author:zhonglin
"""

import os
import sys
import tensorflow as tf

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

tensor_one = tf.constant([1.0, 2.0, 3.0], shape=(3,), name='tensor_one')
tensor_two = tf.constant([5.0, 4.0, 3.0], shape=(3,), name='tensor_two')

tensor_sum = tf.add(tensor_one, tensor_two, name='tensor_sum')

config = tf.ConfigProto(allow_soft_placement=True)
with tf.Session(config=config) as sess:
    sum = sess.run(tensor_sum)
    print(sum)
