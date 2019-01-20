'''
Created on Jan 19, 2019

@author: Ryan Heaton
'''

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

#Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__) # print tensorflow version

fashion_mnist = keras.datasets.fashion_mnist # get fashion mnist from database
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data() # load fashion_mnist to 4 numpy arrays

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',  # array of classification names
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# code to show initial image
'''
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()
'''

# all pixel values are from 0-255
# preproccesing the arrays to be values from 0-1
train_images = train_images / 255.0
test_images = test_images / 255.0

# Diplays first 25 images after preproccesing
# Gives them each names correlating to their label ids
'''
plt.figure(figsize = (10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap = plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()
'''

# Creates a model with layers used to train the algorithm
model = keras.Sequential([
    keras.layers.Flatten(input_shape = (28, 28)), # flattens the 28x28 pixel array to a 784 pixel 1d array
    keras.layers.Dense(128, activation = tf.nn.relu), # creates a 128 neuron dense layer
    keras.layers.Dense(10, activation = tf.nn.softmax) # creates a 10 neuron "softmax" layer to return an array of 10 probability scores
]) 

# compiles the model and adds final settings
model.compile(optimizer = tf.train.AdamOptimizer(), # optimizer for how the model is updates based on the data it sees and its loss function
            loss = 'sparse_categorical_crossentropy', # measures how accurate the model is during training, function minimized to 'steer' model in the right direction
            metrics = ['accuracy']) # monitors testing and training steps, uses 'accuracy', the fraction of images correctly classified

model.fit(train_images, train_labels, epochs = 5) # fits model to training data. Epochs = amount of passes through data

test_loss, test_acc = model.evaluate(test_images,test_labels) # evaluates the model after training on the test data, returning loss and accuracy
print('Test Accuracy: ', test_acc) # prints test accuracy

# MAKING PREDICTIONS

predictions = model.predict(test_images) # predicts label for each test image

# this honestly just sets up the graph, I'm not gonna pretend to know what it means
def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  
  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'
  
  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

# same thing with this guy right here...
def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1]) 
  predicted_label = np.argmax(predictions_array)
 
  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

# sets up and views the i'th image, predictions, and prediction array
'''
i = 12
plt.figure(figsize = (6, 3))
plt.subplot(1, 2, 1)
plot_image(i, predictions, test_labels, test_images)
plt.subplot(1, 2, 2)
plot_value_array(i, predictions, test_labels)
plt.show()
'''

# Plot the first X test images, their predicted label, and the true label
# Color correct predictions in blue, incorrect predictions in red
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions, test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions, test_labels)
plt.show()

# code to predict a single image, and show the array values
img = test_images[0]
img = (np.expand_dims(img, 0)) # turns single image into collection for use in model
predictions_single = model.predict(img)
plot_value_array(0, predictions_single, test_labels) # plots the prediction graph
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()