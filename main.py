import tensorflow as tf

print(tf.__version__)
x = tf.constant([[1, 2, 3], [4, 5, 6]])

print(x)
print(x.shape)
print(x.dtype)
